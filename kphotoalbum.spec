%define version 4.0.0 
%define release %mkrel 0.%revision.2
%define revision 858397

Name:		kphotoalbum
Version:	%{version}
Release:	%{release}
License:	GPLv2+
Url:	        http://www.kphotoalbum.org
Group:		Graphical desktop/KDE
Source0:	http://jaist.dl.sourceforge.net/sourceforge/kphotoalbum/%{name}-r%{revision}.tar.bz2
Patch0:		kphotoalbum-4.0-fix-lib-build.patch
Summary:        K Image Database
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:  kdegraphics4-devel
Obsoletes:      kde4-%name <= 4.0.0
Provides:       kde4-%name = %version

%description
Image database for KDE4

%if %mdkversion < 200900
%post
%{update_desktop_database}
%update_icon_cache hicolor
%endif

%if %mdkversion < 200900
%postun
%{clean_desktop_database}
%clean_icon_cache hicolor
%endif

%files
%defattr(-,root,root)
%{_kde_bindir}/kphotoalbum
%{_kde_datadir}/applications/kde4/*.desktop
%{_kde_appsdir}/kphotoalbum
%{_kde_datadir}/config/kphotoalbumrc
%{_kde_iconsdir}/hicolor/*/*/*

#------------------------------------------------

%prep
%setup -q -n %name
%patch0 -p1

%build
%cmake_kde4 
%make

%install
rm -rf %buildroot
%{makeinstall_std} -C build

%clean
rm -rf %buildroot
