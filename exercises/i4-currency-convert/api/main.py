from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI(title="Currency Convert API")

RATES = {"USD": 1.0, "EUR": 0.93, "INR": 84.5, "GBP": 0.79}


class ConvertBody(BaseModel):
    amount: float = Field(gt=0)
    source: str
    target: str


class ConvertResult(BaseModel):
    amount: float
    source: str
    target: str
    rate: float
    result: float


def normalize(code: str) -> str:
    return code.strip().upper()


def convert(amount: float, source: str, target: str) -> tuple[float, float]:
    s, t = normalize(source), normalize(target)
    if s not in RATES or t not in RATES:
        raise KeyError
    rate = RATES[t] / RATES[s]
    return round(amount * rate, 4), round(rate, 6)


@app.post("/convert", response_model=ConvertResult)
def post_convert(body: ConvertBody) -> ConvertResult:
    try:
        result, rate = convert(body.amount, body.source, body.target)
    except KeyError:
        raise HTTPException(status_code=400, detail="Unsupported currency pair")

    return ConvertResult(
        amount=body.amount,
        source=normalize(body.source),
        target=normalize(body.target),
        rate=rate,
        result=result,
    )


@app.get("/health")
def health():
    return {"ok": True, "currencies": sorted(RATES.keys())}
