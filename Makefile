.PHONY: run-cli clean setup

USER=$(shell whoami)

# Set these accordingly ----------------------
# from nvidia-smi
CUDA_MAJOR_VERSION=13
# pixi binary path
PIXI=/home/$(USER)/.pixi/bin/pixi
# clone of an openfold3 repo, used to find manifest
OPENFOLD3_REPO=/home/$(USER)/code/openfold-3
#---------------------------------------------

MANIFEST=$(OPENFOLD3_REPO)/pixi.toml
ENV=openfold3-cuda$(CUDA_MAJOR_VERSION)-pypi

clean:
	-rm -rf output/
	-rm -rf /tmp/of3-of-kenneyi/

run-cli:
	pixi run -m $(MANIFEST) -e $(ENV) run_openfold predict \
		--query-json ./queries.json \
		--output-dir ./output/ \
		--runner-yaml ./runner.yml


setup:
	$(PIXI) run -m $(MANIFEST) -e $(ENV) setup_openfold
