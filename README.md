# xyz.py

XYZ.py is a Phython 3 command-line interface to work with HERE APIs starting with HERE XYZ Hub APIs.
 
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



