Name:		python-cargo2rpm
Version:	0.3.0
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/c/cargo2rpm/cargo2rpm-%{version}.tar.gz
Summary:	Translation layer between cargo and RPM
URL:		https://pypi.org/project/cargo2rpm/
License:	MIT
Group:		Development/Python
BuildSystem:	python
BuildRequires:	python%{pyver}dist(pip)
BuildArch:	noarch

%description
Translation layer between cargo and RPM

%files
%{_bindir}/cargo2rpm
%{py_sitedir}/cargo2rpm
%{py_sitedir}/cargo2rpm-*.*-info
