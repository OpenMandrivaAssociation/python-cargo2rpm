Name:		python-cargo2rpm
Version:	0.1.15
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/c/cargo2rpm/cargo2rpm-%{version}.tar.gz
Summary:	Translation layer between cargo and RPM
URL:		https://pypi.org/project/cargo2rpm/
License:	MIT
Group:		Development/Python
BuildRequires:	python%{pyver}dist(pip)
BuildArch:	noarch

%description
Translation layer between cargo and RPM

%prep
%autosetup -p1 -n cargo2rpm-%{version}

%build
%py_build

%install
%py_install

%files
%{_bindir}/cargo2rpm
%{py_sitedir}/cargo2rpm
%{py_sitedir}/cargo2rpm-*.*-info
