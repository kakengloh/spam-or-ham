# Spam or Ham

`Spam or Ham` is a simple machine learning **Spam Detection API** that will return:
- `"spam"` if the content **is** a spam
- `"ham"` if the content **is not** a spam

It is based on the **Naive Bayes** classification method.

## Examples
```json
// POST /detect
{
  "content": "Hello world"
}

// Response
"ham"
```
```json
// POST /detect
{
  "content": "Click Here Now ! Simply Amateur Just like the girl next door. XXX Free Tour!"
}

// Response
"spam"
```

## Installation (using conda)

Create and activate conda environment

```bash
conda env create -f environment.yml --prefix .venv
conda activate ./.venv
```

## Get started 🚀

Runs the server
```bash
uvicorn app.main:app --reload
```
- Server should be running on [localhost:8000](http://localhost:8000)
- API docs can be viewed at [localhost:8000/docs](http://localhost:8000/docs)

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)