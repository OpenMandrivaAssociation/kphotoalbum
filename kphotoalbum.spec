Summary:	K Image Database
Name:		kphotoalbum
Version:	5.12.0
Release:	1
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		http://www.kphotoalbum.org
Source0:	http://download.kde.org/stable/kphotoalbum/%{version}/%{name}-%{version}.tar.xz

BuildRequires:  appstream
BuildRequires:  gettext
BuildRequires:	marble-devel
BuildRequires:	pkgconfig(exiv2)
BuildRequires:	cmake(KF5Kipi)
BuildRequires:	cmake(KF5KDcraw)
BuildRequires:	cmake(KF5CoreAddons)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5KIO)
BuildRequires:	cmake(KF5DocTools)
BuildRequires:	cmake(KF5WidgetsAddons)
BuildRequires:	cmake(KF5Config)
BuildRequires:	cmake(KF5IconThemes)
BuildRequires:	cmake(KF5Archive)
BuildRequires:	cmake(KF5Parts)
BuildRequires:	cmake(KF5JobWidgets)
BuildRequires:	cmake(KF5KDcraw)
BuildRequires:	cmake(KF5Kipi)
BuildRequires:	cmake(KF5KExiv2)
BuildRequires:	cmake(KF5Purpose)
BuildRequires:	cmake(Phonon4Qt5)
BuildRequires:	pkgconfig(Qt5Sql)
BuildRequires:	pkgconfig(Qt5Xml)
BuildRequires:	pkgconfig(Qt5Widgets)
BuildRequires:	pkgconfig(Qt5Network)
BuildRequires:  cmake(Qt5Test)
BuildRequires:  cmake(qtav)
BuildRequires:	pkgconfig(libjpeg)

%description
Image database for KF5.

%files -f %{name}.lang
%{_bindir}/kphotoalbum
%{_bindir}/kpa-backup.sh
%{_bindir}/kpa-thumbnailtool
%{_bindir}/open-raw.pl
%{_libdir}/libkpabase.so
%{_libdir}/libkpaexif.so
%{_libdir}/libkpathumbnails.so
%{_datadir}/applications/*.desktop
%{_datadir}/metainfo/org.kde.kphotoalbum.appdata.xml
%{_datadir}/kphotoalbum
#{_datadir}/kxmlgui5/kphotoalbum
%{_sysconfdir}/xdg/kphotoalbumrc
%{_iconsdir}/hicolor/*/*/*

#------------------------------------------------

%prep
%autosetup -p1
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

%find_lang %{name} --with-html

