%define version 4.1.1
%define release %mkrel 5

Name:		kphotoalbum
Version:	%{version}
Release:	%{release}
License:	GPLv2+
Url:	        http://www.kphotoalbum.org
Group:		Graphical desktop/KDE
Source:		http://www.kphotoalbum.org/data/download/%{name}-%{version}.tar.bz2
Patch0:		kphotoalbum-4.1.1-r1118420.patch
Patch1:		kphotoalbum-4.1.1-r1120711.patch
Patch2:		kphotoalbum-4.1.1-r1118926.patch
Patch3:		kphotoalbum-4.1.1-r1119917.patch
Patch4:		kphotoalbum-4.1.1-r1120248.patch
Patch5:		kphotoalbum-4.1.1-r1118507.patch
Patch6:		kphotoalbum-4.1.1-exiv2.patch
Summary:        K Image Database
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:  kdegraphics4-devel
Obsoletes:      kde4-%name <= 4.0.0
Provides:       kde4-%name = %version

%description
Image database for KDE4.

%files -f %name.lang
%defattr(-,root,root)
%{_kde_bindir}/kphotoalbum
%{_kde_datadir}/applications/kde4/*.desktop
%{_kde_appsdir}/kphotoalbum
%{_kde_datadir}/config/kphotoalbumrc
%{_kde_iconsdir}/hicolor/*/*/*

#------------------------------------------------

%prep
%setup -q -n %name-%version
pushd doc
%patch0 -p5
popd
pushd doc-translations/de_kphotoalbum
%patch1 -p5
popd
pushd doc-translations/et_kphotoalbum
%patch2 -p5
popd
pushd doc-translations/it_kphotoalbum
%patch3 -p5
popd
pushd doc-translations/sv_kphotoalbum
%patch4 -p5
popd
pushd doc-translations/uk_kphotoalbum
%patch5 -p5
popd
%patch6 -p4

%build
%cmake_kde4 
%make

%install
rm -rf %buildroot
%{makeinstall_std} -C build

%find_lang %name --with-html

%clean
rm -rf %buildroot
