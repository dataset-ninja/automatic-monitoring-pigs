Dataset **Automatic Monitoring of Pigs** can be downloaded in [Supervisely format](https://developer.supervisely.com/api-references/supervisely-annotation-json-format):

 [Download](https://assets.supervisely.com/remote/eyJsaW5rIjogImZzOi8vYXNzZXRzLzE5MThfQXV0b21hdGljIE1vbml0b3Jpbmcgb2YgUGlncy9hdXRvbWF0aWMtbW9uaXRvcmluZy1vZi1waWdzLURhdGFzZXROaW5qYS50YXIiLCAic2lnIjogInlpY3RQeGVLWU9GWlRwVDlYd1RKazh6SUdCYjJsdjVGQmNZS0VyZHpsclE9In0=)

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