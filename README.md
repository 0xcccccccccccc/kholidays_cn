# kholidays_cn

法定节假日-KHolidays自动生成脚本，感谢 [chinese-calendar](https://github.com/LKI/chinese-calendar) 的贡献者多年来持续维护法定节假日规则。

制作这个脚本目的是修复Archlinux KDE Plasma日历下残缺多年的假期数据。

## 测试

目前Archlinux的主线KDE停留在QT5阶段，上游KHoliday更新不一定会backport到kholiday5上，因此这里提供一个PKGBUILD，makepkg产物（kholiday5-cn）可以替代kholiday5。安装后日历即可显示2004-2024的节假日。

你也可以到[aur](https://aur.archlinux.org/packages/kholidays5-cn)找到这个包

## TODO

- CheckSum校验
- 从其他来源补充cultural日期（七夕重阳等不放假节日）
- Actions自动Push到主线仓库
