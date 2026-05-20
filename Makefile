.PHONY: run run-cli clean setup

ENV=openfold3-cuda13-pypi
MANIFEST=/home/kenneyi/code/openfold-3/pixi.toml
PIXI=/home/kenneyi/.pixi/bin/pixi

clean:
	-rm -rf output/
	-rm -rf /tmp/of3-of-kenneyi/

run:
	$(PIXI) run -m $(MANIFEST) -e $(ENV) python run_inference.py

run-cli:
	pixi run -m $(MANIFEST) -e $(ENV) run_openfold predict \
		--query-json ./queries.json \
		--output-dir ./output/ \
		--runner-yaml ./runner.yml


setup:
	$(PIXI) run -m $(MANIFEST) -e $(ENV) setup_openfold
