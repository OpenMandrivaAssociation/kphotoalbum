Name:		kphotoalbum
Version:	4.3
Release:	1
Summary:	K Image Database
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		http://www.kphotoalbum.org
Source:		http://www.kphotoalbum.org/data/download/%{name}-%{version}.tar.bz2
BuildRequires:	pkgconfig(libkexiv2)
BuildRequires:	pkgconfig(libkdcraw)
BuildRequires:	pkgconfig(libkipi)
BuildRequires:	marble-devel
BuildRequires:	kdelibs4-devel

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

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

%find_lang %{name} --with-html

