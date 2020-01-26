# TinyML gen

This is a simple package to export a model trained in Tensorflow Lite
to a plain C array, ready to be used for inference on microcontrollers.

### Install

```shell script
pip install tinymlgen
```

### Use

```python
from tinymlgen import port

if __name__ == '__main__':
    tf_model = create_tf_model()
    c_code = port(tf_model)
```

### Configuration

You can pass a few parameters to the `port` function:

 - `optimize (=True)`: apply optimizers to the exported model.
    Can either be a list of optimizers or a boolean, in which case
    `OPTIMIZE_FOR_SIZE` is applied
 - `variable_name (='model_data')`: give the exported array a custom name
 - `pretty_print (=False)`: print the array in a nicely formatted arrangement


