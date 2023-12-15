# Documentation

The documentation is built using
[Sphinx](https://www.sphinx-doc.org/en/master/).

Install the documentation dependencies
```bash
poetry install --with docs
```

Build the documentation
```bash
cd docs/
poetry run make html
```

The documentation will be built in `build/html/`
```bash
python -m http.server --directory build/html/
```

Generate the API Reference
```bash
poetry run sphinx-apidoc -o docs/source pytrello2/
```
