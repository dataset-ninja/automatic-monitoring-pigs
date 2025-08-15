Dataset **Automatic Monitoring of Pigs** can be downloaded in [Supervisely format](https://developer.supervisely.com/api-references/supervisely-annotation-json-format):

 [Download](https://assets.supervisely.com/remote/eyJsaW5rIjogInMzOi8vc3VwZXJ2aXNlbHktZGF0YXNldHMvMTkxOF9BdXRvbWF0aWMgTW9uaXRvcmluZyBvZiBQaWdzL2F1dG9tYXRpYy1tb25pdG9yaW5nLW9mLXBpZ3MtRGF0YXNldE5pbmphLnRhciIsICJzaWciOiAiVjY5R0dDN29LMndOcVNxK1E1NUgvRmxjaXlnNm9Ob1pEQVBGTXVJcDQ2TT0ifQ==?response-content-disposition=attachment%3B%20filename%3D%22automatic-monitoring-of-pigs-DatasetNinja.tar%22)

As an alternative, it can be downloaded with *dataset-tools* package:
``` bash
pip install --upgrade dataset-tools
```

... using following python code:
``` python
import dataset_tools as dtools

dtools.download(dataset='Automatic Monitoring of Pigs', dst_dir='~/dataset-ninja/')
```
Make sure not to overlook the [python code example](https://developer.supervisely.com/getting-started/python-sdk-tutorials/iterate-over-a-local-project) available on the Supervisely Developer Portal. It will give you a clear idea of how to effortlessly work with the downloaded dataset.

The data in original format can be [downloaded here](https://drive.google.com/file/d/1DmkR5AyysQkFbMEwjPjJnnNVyGvtsu9H/view).