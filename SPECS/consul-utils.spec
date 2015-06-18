Name:		consul-utils
Version:	0.1.1
Release:	2%{?dist}
Summary:	Command line tools for Consul

%global consulkv_version 0.1.1
%global consulacl_version 0.1.1

Group:		Applications/System
License:	ASL 2.0
Source0:	https://github.com/CiscoCloud/consulacl/releases/download/v%{consulacl_version}/consulacl_%{consulacl_version}_linux_amd64.tar.gz
Source1:	https://github.com/CiscoCloud/consulkv/releases/download/v%{consulkv_version}/consulkv_%{consulkv_version}_linux_amd64.tar.gz

%description
Command line tools for Consul

%prep
%setup -T -b 0 -n consulacl_%{consulacl_version}_linux_amd64
%setup -T -b 1 -n consulkv_%{consulkv_version}_linux_amd64

%install
mkdir -p %{buildroot}/%{_bindir}
cp consulkv %{buildroot}/%{_bindir}
cd ../consulacl_%{consulacl_version}_linux_amd64
cp consulacl %{buildroot}/%{_bindir}

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)
%attr(755, root, root) %{_bindir}/consulkv
%attr(755, root, root) %{_bindir}/consulacl
