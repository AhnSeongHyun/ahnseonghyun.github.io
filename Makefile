# Makefile for ash84.io static site

.PHONY: build clean run


# Build the static site
build: 
	zvc build
	echo "ash84.io" > ./docs/CNAME
	echo "google.com, pub-8699046198561974, DIRECT, f08c47fec0942fa0" > ./docs/ads.txt

# Clean generated files
clean: 
	zvc clean

run: 
	zvc build
	python -m http.server 8000  --directory ./docs 
 