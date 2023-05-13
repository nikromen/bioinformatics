%global srcname bioframe

Name:           python-%{srcname}
Version:        0.4.1
Release:        1%{?dist}
Summary:        Pandas utilities for tab-delimited and other genomic files

License:        MIT
URL:            https://github.com/open2c/%{srcname}
Source:         %{url}/archive/refs/tags/v%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel

# for check section
BuildRequires:  python3dist(pytest)


%description
%{summary}


%package -n     python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname}
%{summary}


%prep
%autosetup -n %{srcname}-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files %{srcname}


%check
%pyproject_check_import
%pytest


%files -n python3-%{srcname} -f %{pyproject_files}


%changelog
* Sat May 13 2023 Jiri Kyjovsky <j1.kyjovsky@gmail.com> - 0.4.1-1
- Initial package
