%define version 4.0.0 
%define release %mkrel 0.%revision.1
%define revision 744030

Name:		kphotoalbum
Version:	%{version}
Release:	%{release}
License:	GPLv2+
Url:	        http://www.kphotoalbum.org
Group:		Graphical desktop/KDE
Source0:	http://jaist.dl.sourceforge.net/sourceforge/kphotoalbum/%{name}-%version.%revision.tar.bz2
Summary:        K Image Database
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:  kdelibs4-devel
Obsoletes:      kde4-%name <= 4.0.0
Provides:       kde4-%name = %version


%description
Image database for KDE4

%post
%{update_desktop_database}
%update_icon_cache hicolor

%postun
%{clean_desktop_database}
%clean_icon_cache hicolor

%files
%defattr(-,root,root)
%{_kde_bindir}/kphotoalbum
%{_kde_datadir}/applications/kde4/kphotoalbum-import.desktop
%{_kde_datadir}/applications/kde4/kphotoalbum.desktop
%dir %{_kde_appsdir}/kphotoalbum
%{_kde_appsdir}/kphotoalbum/default-layout.xml
%{_kde_appsdir}/kphotoalbum/default-setup
%dir %{_kde_appsdir}/kphotoalbum/demo
%dir %{_kde_appsdir}/kphotoalbum/demo/CategoryImages
%{_kde_appsdir}/kphotoalbum/demo/CategoryImages/*.jpg
%{_kde_appsdir}/kphotoalbum/demo/*.jpg
%{_kde_appsdir}/kphotoalbum/demo/*.db
%{_kde_appsdir}/kphotoalbum/demo/*.xml
%{_kde_appsdir}/kphotoalbum/demo/*.avi
%{_kde_appsdir}/kphotoalbum/kphotoalbumui.rc
%dir %{_kde_appsdir}/kphotoalbum/pics
%{_kde_appsdir}/kphotoalbum/pics/*.png
%{_kde_appsdir}/kphotoalbum/pics/*.jpg
%dir %{_kde_appsdir}/kphotoalbum/themes
%dir %{_kde_appsdir}/kphotoalbum/themes/blue
%{_kde_appsdir}/kphotoalbum/themes/blue/*.png
%{_kde_appsdir}/kphotoalbum/themes/blue/*.html
%{_kde_appsdir}/kphotoalbum/themes/blue/*.theme
%{_kde_appsdir}/kphotoalbum/themes/blue/*.css
%dir %{_kde_appsdir}/kphotoalbum/themes/grey
%{_kde_appsdir}/kphotoalbum/themes/grey/*.png
%{_kde_appsdir}/kphotoalbum/themes/grey/*.html
%{_kde_appsdir}/kphotoalbum/themes/grey/*.theme
%{_kde_appsdir}/kphotoalbum/themes/grey/*.css
%dir %{_kde_appsdir}/kphotoalbum/themes/rounded
%{_kde_appsdir}/kphotoalbum/themes/rounded/*.png
%{_kde_appsdir}/kphotoalbum/themes/rounded/*.png
%{_kde_appsdir}/kphotoalbum/themes/rounded/*.html
%{_kde_appsdir}/kphotoalbum/themes/rounded/*.theme
%{_kde_appsdir}/kphotoalbum/themes/rounded/*.css
%{_kde_appsdir}/kphotoalbum/tips
%{_kde_datadir}/config/kphotoalbumrc
%{_kde_iconsdir}/hicolor/*/*/*.png

#------------------------------------------------

%prep
%setup -q -n %name-%version

%build
%cmake_kde4 
%make

%install
cd build
rm -rf %buildroot
%{makeinstall_std}


%clean
rm -rf %buildroot
