%define version 4.0.2
%define release %mkrel 3

Name:		kphotoalbum
Version:	%{version}
Release:	%{release}
License:	GPLv2+
Url:	        http://www.kphotoalbum.org
Group:		Graphical desktop/KDE
Source:		http://kphotoalbum.org/data/download/%name-4.0.2-kde4.3.1.tar.bz2
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
%setup -q -n %name-4.3.1

%build
%cmake_kde4 
%make

%install
rm -rf %buildroot
%{makeinstall_std} -C build

%find_lang %name

%clean
rm -rf %buildroot
