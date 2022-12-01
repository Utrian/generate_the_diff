[![Actions Status](https://github.com/Utrian/python-project-50/workflows/hexlet-check/badge.svg)](https://github.com/Utrian/python-project-50/actions)
[![GitHub Actions](https://github.com/Utrian/python-project-50/actions/workflows/pyci.yml/badge.svg)](https://github.com/Utrian/python-project-50/actions/workflows/pyci.yml)
[![Maintainability](https://api.codeclimate.com/v1/badges/d7f5da7657fe940d6af3/maintainability)](https://codeclimate.com/github/Utrian/python-project-50/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/d7f5da7657fe940d6af3/test_coverage)](https://codeclimate.com/github/Utrian/python-project-50/test_coverage)


# **Gendiff** - compare two json and/or yaml files

## **About**
You can get a comparison of two json/yaml files - different formats can be compared too!


The output type depends on the selected format:
- **stylish** - is selected by default
- **plain**
- **json**


## **Install**
```bash
git clone https://github.com/Utrian/python-project-50
cd python-project-50
make install
```

## Help
```bash
gendiff -h

usage: gendiff [-h] [-f [{stylish,plain,json}]] [first_file] [second_file]

Compares two configuration files and shows a difference.

positional arguments:
  first_file
  second_file

optional arguments:
  -h, --help            show this help message and exit
  -f [{stylish,plain,json}], --format [{stylish,plain,json}]
                        set format of output
```

## **Examples of output**
There are test files for you, their paths:
* files/json/first_file.json
* files/json/second_file.json
* files/yaml/first_file.yaml
* files/yaml/second_file.yaml
  
They can be used like this:
```bash
gendiff -f stylish files/json/first_file.json files/yaml/second_file.yaml
```

### **Stylish format mode**

*The conditional both-values:*
symbol | description
:------|:------------
\-     | if the parameter was deleted from the first file;
\+     | if the parameter was added in second_file;
  || (blank) if the parameter has not been changed or if it is a nested string that is in both files;
   
If the file value has been changed, the first value in the output will be the value from the first file, then the second.
  
**Command**
(It is not necessary to specify the format to use it.)

```bash
gendiff path_first_file path_second_file
```
**Output**
```bash
{
    common: {
      + follow: false
        setting1: Value 1
      - setting2: 200
      - setting3: true
      + setting3: null
    }
}
```

### **Plain format mode**
Only parameters that have been changed are shown. Unchanged parameters and nested structures that are in both files are not shown.

**Command**
```bash
gendiff -f plain path_first_file path_second_file
```

**Output**
```bash
Property 'common.follow' was added with value: false
Property 'common.setting2' was removed
Property 'common.setting3' was updated. From true to null
Property 'common.setting4' was added with value: 'blah blah'
```

### **Json format mode**
In this format you can see the internal representation of the difference of the two files.

**Command**
```bash
gendiff -f json path_first_file path_second_file
```
**Output**
```bash
[
  {
    "type": "nested",
    "key": "common",
    "children": [
      {
        "type": "added",
        "key": "follow",
        "value": "false"
      }
    ]
  }
]
```