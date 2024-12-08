Summary:	K Image Database
Name:		kphotoalbum
Version:	6.0.0
Release:	1
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		https://www.kphotoalbum.org
Source0:	http://download.kde.org/stable/kphotoalbum/%{version}/%{name}-%{version}.tar.xz

BuildRequires:  appstream
BuildRequires:  gettext
BuildRequires:	plasma6-marble-devel
BuildRequires:	pkgconfig(exiv2)
BuildRequires:	cmake(KF6CoreAddons)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6KIO)
BuildRequires:	cmake(KF6DocTools)
BuildRequires:	cmake(KF6WidgetsAddons)
BuildRequires:	cmake(KF6Config)
BuildRequires:	cmake(KF6IconThemes)
BuildRequires:	cmake(KF6Archive)
BuildRequires:	cmake(KF6Parts)
BuildRequires:	cmake(KF6JobWidgets)
BuildRequires:	cmake(KF6Purpose)
BuildRequires:	cmake(Phonon4Qt6)
BuildRequires:	pkgconfig(Qt6Sql)
BuildRequires:	pkgconfig(Qt6Xml)
BuildRequires:	pkgconfig(Qt6Widgets)
BuildRequires:	pkgconfig(Qt6Network)
BuildRequires:  cmake(Qt6Test)
BuildRequires:	pkgconfig(libjpeg)

%description
Image database for KF6.

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

