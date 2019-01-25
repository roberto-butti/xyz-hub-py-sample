# xyz-samples.py

This is a set of samples written with Python 3 for the integration with HERE XYZ Hub APIs.
If you are looking for the official CLI tools, please take a look there :
[HERE CLI (Official Node.js)](https://www.npmjs.com/package/@here/cli).


## Useful links
- [HERE XYZ Hub APIs](https://www.here.xyz/api/)
- [Swagger](https://xyz.api.here.com/hub/static/swagger/)
- [HERE CLI (Official Node.js)](https://www.npmjs.com/package/@here/cli)

 
## Installing the command

```bash
pip install -r requirements.txt
```

## Usage

### Exploring projects

```
python xyz.py project
```

### Exploring a project

```
python xyz.py project --pid <pid>
```
where *pid* is a valid project identifier. The projects needs to be published.

### Retrieving Project's Spaces

```
python xyz.py project --pid <pid> --spaces
```
where *pid* is a valid project identifier. The projects needs to be published.


### Exploring a space
```
python xyz.py space --sid <sid> --rot <rot>
```
where
- *sid* is a valid space identifier
- *rot* is the Read Only Token retrieved from the project

### Exploring space's features
```
python xyz.py feature --sid <sid> --rot <rot>
```
where
- *sid* is a valid space identifier
- *rot* is the Read Only Token retrieved from the project



