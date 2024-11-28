# kholidays_cn

法定节假日-KHolidays自动生成脚本，感谢 [chinese-calendar](https://github.com/LKI/chinese-calendar) 的贡献者多年来持续维护法定节假日规则。

制作这个脚本目的是修复Archlinux KDE Plasma日历下残缺多年的假期数据。

## 测试

这里提供一个PKGBUILD模板（make_pkgbuild.py），makepkg产物（kholiday5-cn）可以替代kholiday5。安装后日历即可显示2004-今年的节假日，只要chinese-calendar还更新，这个仓库就能自动跟上。

你也可以到[aur](https://aur.archlinux.org/packages/kholidays5-cn)找到这个包

目前archlinux已经不再需要kholidays5，不需要手动安装这里提供的包。

## TODO

- ~~CheckSum校验~~
- 从其他来源补充cultural日期（七夕重阳等不放假节日）
- ~~Actions自动Push到主线仓库~~
