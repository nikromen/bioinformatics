Name:           velvet
Version:        1.2.10
Release:        1%{?dist}
Summary:        Short read de novo assembler using de Bruijn graphs

License:        GPLv2
URL:            https://github.com/dzerbino/%{name}
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz

BuildArch:      x86_64

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  zlib-devel
BuildRequires:  make


%description
%{summary}


%prep
%autosetup


%build
make CFLAGS="-fPIE %{optflags}"


%install
rm -rf %{buidroot}
mkdir -p %{buildroot}%{_bindir}
install -p -m 0775 %{name}g %{buildroot}%{_bindir}
install -p -m 0775 %{name}h %{buildroot}%{_bindir}


%files
%{_bindir}/%{name}g
%{_bindir}/%{name}h


%changelog
* Sat May 13 2023 Jiri Kyjovsky <j1.kyjovsky@gmail.com>
- Initial package
