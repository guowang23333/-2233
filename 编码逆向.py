from urllib.parse import quote

original_string = "/wEdAAOSZd7JSA7TmyAe+1DuvWd3POqWis/6SsFlie7YKY+xcHTntDN4bawON3TdT0LQZSUgLfAAhnAacVLNEN3xRXIMKv3bt7CT6TO+oKlzEB/gYg=="

# 使用quote进行编码
encoded_string = quote(original_string)

print(encoded_string)
# 输出: "Hello%20World%21"
