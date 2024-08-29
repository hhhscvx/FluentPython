from functools import partial

from html_tag_generator import tag


picture = partial(tag, 'img', class_='pic-frame')


print(picture(src='musasi.jpg'))
print(picture.func)
