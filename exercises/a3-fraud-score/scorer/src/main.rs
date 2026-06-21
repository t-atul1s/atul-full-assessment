use serde::{Deserialize, Serialize};

#[derive(Debug, Deserialize)]
struct Event {
    event_id: String,
    account_id: String,
    value: f64,
    channel: String,
}

#[derive(Debug, Serialize, PartialEq)]
struct Score {
    event_id: String,
    score: f64,
    band: String,
    flags: Vec<String>,
}

pub fn score_event(ev: &Event) -> Score {
    let mut score = 0.0;
    let mut flags = Vec::new();

    if ev.value > 5000.0 {
        score += 0.45;
        flags.push("high_value".into());
    } else if ev.value > 1000.0 {
        score += 0.2;
        flags.push("elevated_value".into());
    }

    match ev.channel.as_str() {
        "wire" | "crypto" => {
            score += 0.35;
            flags.push(format!("risky_channel_{}", ev.channel));
        }
        "atm" => score += 0.1,
        _ => {}
    }

    if score > 1.0 {
        score = 1.0;
    }

    let band = if score < 0.25 {
        "low"
    } else if score <= 0.6 {
        "medium"
    } else {
        "high"
    };

    Score {
        event_id: ev.event_id.clone(),
        score,
        band: band.to_string(),
        flags,
    }
}

fn main() {
    use std::io::{self, Read};
    let mut buf = String::new();
    io::stdin().read_to_string(&mut buf).expect("stdin");
    let ev: Event = serde_json::from_str(&buf).expect("json");
    let out = score_event(&ev);
    println!("{}", serde_json::to_string(&out).unwrap());
}

#[cfg(test)]
mod tests {
    use super::*;

    fn ev(value: f64, channel: &str) -> Event {
        Event {
            event_id: "ev-1".into(),
            account_id: "a".into(),
            value,
            channel: channel.into(),
        }
    }

    #[test]
    fn small_web_is_low() {
        let s = score_event(&ev(100.0, "web"));
        assert!(s.score < 0.25);
        assert_eq!(s.band, "low");
    }

    #[test]
    fn wire_high_value_is_high() {
        let s = score_event(&ev(9000.0, "wire"));
        assert_eq!(s.band, "high");
    }
}
