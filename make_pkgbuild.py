import datetime
import hashlib
if __name__ == "__main__":
    with (open("PKGBUILD", "w") as f_output,
          open("PKGBUILD.tmpl", "r") as f_template,
          open("holiday_cn_zh-cn", "rb") as f_holiday):
        template = f_template.read()
        f_output.write(template.replace(
            "{{date}}", datetime.datetime.now().strftime("%Y%m%d")
        ).replace(
            "{{holiday_sha256sum}}", hashlib.sha256(f_holiday.read()).hexdigest()
        ))
