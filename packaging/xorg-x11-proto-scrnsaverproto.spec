
Name:       xorg-x11-proto-scrnsaverproto
Summary:    X.Org X11 Protocol scrnsaverproto
Version:    1.2.1
Release:    1
Group:      Development/System
License:    MIT
URL:        http://www.x.org
Source0:    http://xorg.freedesktop.org/releases/individual/proto/scrnsaverproto-%{version}.tar.gz
Source1001: packaging/xorg-x11-proto-scrnsaverproto.manifest 
Provides:   scrnsaverproto
BuildRequires: pkgconfig(xorg-macros)


%description
Description: %{summary}



%prep
%setup -q -n %{name}-%{version}

%build
cp %{SOURCE1001} .

%reconfigure --disable-static \
    --libdir=%{_datadir}

# Call make instruction with smp support
make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install


%clean
rm -rf %{buildroot}






%files
%manifest xorg-x11-proto-scrnsaverproto.manifest
%defattr(-,root,root,-)
%{_datadir}/pkgconfig/scrnsaverproto.pc
%{_docdir}/scrnsaverproto/saver.xml
%{_includedir}/X11/extensions/saver.h
%{_includedir}/X11/extensions/saverproto.h


