Summary: NethServer configuration for password policies
Name: nethserver-password
Version: 1.0.1
Release: 1%{?dist}
License: GPL
Source: %{name}-%{version}.tar.gz
BuildArch: noarch
URL: http://dev.nethserver.org/projects/nethforge/wiki/%{name}
BuildRequires: nethserver-devtools

AutoReq: no
Requires: nethserver-directory


%description
NethServer configuration for password policies

%prep
%setup

%post

%preun

%build
%{makedocs}
perl createlinks

%install
rm -rf $RPM_BUILD_ROOT
(cd root   ; find . -depth -print | cpio -dump $RPM_BUILD_ROOT)

%{genfilelist} $RPM_BUILD_ROOT > e-smith-%{version}-filelist

%clean 
rm -rf $RPM_BUILD_ROOT

%files -f e-smith-%{version}-filelist
%defattr(-,root,root)

%changelog
* Mon Apr 6 2015 Stephane de Labrusse <stephdl@de-labrusse.fr> - 1.0.1-1-ns6
- Action created to merge PassExpire2yes with user-{modify,create}

* Sat Apr 4 2015 Stephane de Labrusse <stephdl@de-labrusse.fr> - 1.0.0-5-ns6
- Initial release
