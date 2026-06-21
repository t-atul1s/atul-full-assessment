.PHONY: verify bootstrap test

verify:
	@chmod +x scripts/verify-all.sh exercises/d5-bootstrap/bootstrap.sh
	@./scripts/verify-all.sh

bootstrap:
	@chmod +x exercises/d5-bootstrap/bootstrap.sh
	@./exercises/d5-bootstrap/bootstrap.sh

test: verify
