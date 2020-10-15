import platform

if platform.system() == 'Linux':
    DATE_DATA_FRAME_FORMAT: str = '%-m/%-d/%y'
elif platform.system() == 'Windows':
    DATE_DATA_FRAME_FORMAT: str = '%#m/%#d/%y'
else:
    DATE_DATA_FRAME_FORMAT: str = '%-m/%-d/%y'
