%global debug_package %{nil}

Name:           mafft
Version:        7.520
Release:        1%{?dist}
Summary:        Multiple sequence alignment program

License:        BSD
URL:            https://gitlab.com/sysimm/%{name}
Source0:        %{url}/-/archive/v%{version}/%{name}-v%{version}.tar.gz

BuildArch:      x86_64

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  zlib-devel
BuildRequires:  make


%description
%{summary}


%prep
%autosetup -n %{name}-v%{version}


%build
cd core
make clean
make CFLAGS="-fPIE %{optflags}"
cd ../extensions
make clean
make CFLAGS="-fPIE %{optflags}"
cd ..


%install
rm -rf %{buidroot}
cd core
%make_install CFLAGS="-fPIE %{optflags}"
cd ../extensions
%make_install CFLAGS="-fPIE %{optflags}"
cd ..


%files
# https://gitlab.com/sysimm/mafft/-/tree/main#install-select-a-or-b-below
# no macros to it?
%{_prefix}/*


%changelog
* Sat Mar 04 2023 Jiri Kyjovsky <j1.kyjovsky@gmail.com>
- Initial package
