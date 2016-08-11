Summary:	K Image Database
Name:		kphotoalbum
Version:	4.7.2
Release:	1
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		http://www.kphotoalbum.org
Source0:	http://download.kde.org/stable/kphotoalbum/%{version}/src/%{name}-%{version}.tar.xz
Patch1:		kphotoalbum-4.7.1-clang.patch

BuildRequires:	kdelibs4-devel
BuildRequires:	marble-devel
BuildRequires:	pkgconfig(exiv2)
BuildRequires:	pkgconfig(libkdcraw)
BuildRequires:	pkgconfig(libkipi)

%description
Image database for KDE4.

%files -f %{name}.lang
%{_kde_bindir}/kphotoalbum
%{_kde_bindir}/kpa-backup.sh
%{_kde_bindir}/open-raw.pl
%{_kde_applicationsdir}/*.desktop
%{_kde_appsdir}/kphotoalbum
%{_kde_datadir}/config/kphotoalbumrc
%{_kde_iconsdir}/hicolor/*/*/*

#------------------------------------------------

%prep
%setup -q
%apply_patches

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

%find_lang %{name} --with-html

