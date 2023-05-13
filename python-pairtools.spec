%global srcname pairtools

Name:           python-%{srcname}
Version:        1.0.2
Release:        1%{?dist}
Summary:        CLI tools to process mapped Hi-C data

License:        MIT
URL:            https://github.com/open2c/%{srcname}
Source:         %{pypi_source %{srcname}}

BuildArch:      noarch
BuildRequires:  python3-devel


%description
%{summary}


%package -n     python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname}
%{summary}


%prep
%autosetup -n %{srcname}-%{version}


%generate_buildrequires
%pyproject_buildrequires -r


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
* Sat May 13 2023 Jiri Kyjovsky <j1.kyjovsky@gmail.com> - 1.0.2-1
- Initial package
