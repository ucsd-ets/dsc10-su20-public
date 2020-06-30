.PHONY: artifacts
artifacts:
	mkdir -p _build/artifacts
	cd _build/artifacts && ../../../__support__/bin/publish ../../../lectures --meta lectures.json
