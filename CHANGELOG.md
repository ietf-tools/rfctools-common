# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [v0.7.0] - 2026-04-24
### :sparkles: New Features
- [`b75878f`](https://github.com/ietf-tools/rfctools-common/commit/b75878f9dfaf69b90e3c8a9c6546073cfc8fa889) - Migrate to pyproject.toml *(PR [#17](https://github.com/ietf-tools/rfctools-common/pull/17) by [@bkmgit](https://github.com/bkmgit))*
  - :arrow_lower_right: *addresses issue [#16](https://github.com/ietf-tools/rfctools-common/issues/16) opened by [@bkmgit](https://github.com/bkmgit)*

### :bug: Bug Fixes
- [`a787ad6`](https://github.com/ietf-tools/rfctools-common/commit/a787ad6ba78be29a47bc0d0b61e64e78c3d5dd90) - Remove old changelog parsing and MANIFEST.in *(PR [#11](https://github.com/ietf-tools/rfctools-common/pull/11) by [@moonshiner](https://github.com/moonshiner))*

### :construction_worker: Build System
- [`d39ee8b`](https://github.com/ietf-tools/rfctools-common/commit/d39ee8bcee02365c39b853f85ff848501e2145dd) - Add 'pyflakes' to test dependencies *(PR [#18](https://github.com/ietf-tools/rfctools-common/pull/18) by [@kesara](https://github.com/kesara))*
- [`2f8b740`](https://github.com/ietf-tools/rfctools-common/commit/2f8b740e02754006111340991a7700fe124d2362) - Add PyPI publish workflow *(PR [#20](https://github.com/ietf-tools/rfctools-common/pull/20) by [@kesara](https://github.com/kesara))*
  - :arrow_lower_right: *addresses issue [#19](https://github.com/ietf-tools/rfctools-common/issues/19) opened by [@kesara](https://github.com/kesara)*

### :memo: Documentation Changes
- [`92ce001`](https://github.com/ietf-tools/rfctools-common/commit/92ce0019f8039895669f8dcb456423699632d78b) - reformat README.md *(commit by [@NGPixel](https://github.com/NGPixel))*
- [`bd0b04b`](https://github.com/ietf-tools/rfctools-common/commit/bd0b04b3dca4b0ba7d12807e059bab800df1adc6) - fix LICENSE *(commit by [@NGPixel](https://github.com/NGPixel))*
- [`ec512c4`](https://github.com/ietf-tools/rfctools-common/commit/ec512c4ee2dd68413654a84f26f0ae04c712ac21) - reformat CHANGELOG.md *(commit by [@NGPixel](https://github.com/NGPixel))*
- [`7a4c929`](https://github.com/ietf-tools/rfctools-common/commit/7a4c929d726ba4dd55aad4e4b2da70638381dc1f) - update README logo *(commit by [@NGPixel](https://github.com/NGPixel))*

### :wrench: Chores
- [`0a4f7a7`](https://github.com/ietf-tools/rfctools-common/commit/0a4f7a7a1a00cb24b8ddd87f3f16f8e9eabdb4f0) - exclude non-rfctools-common files *(commit by [@NGPixel](https://github.com/NGPixel))*


## [0.6.1] - 2020-01-24

### Removed

- Remove module six from the setup

## [0.6.0] - 2019-10-10

### Changed

- Update to the latest set of schema files
- Update the entity definition file with more values

## [0.5.17] - 2019-08-16

### Removed

- Remove Python 3.4 from the supported liste

## [0.5.16] - 2019-07-01

### Changed

- Update the RNG schema file from XML2RFC drop v2.23.0

## [0.5.15] - 2019-05-27

### Changed

- Use the correct function anywhere that we could write out UTF-8

## [0.5.14] - 2019-04-21

### Changed

- Merge in some of the XML2RFC changes to these files
- Setup to allow for the input coming from stdin
- Clean things up so that pyflakes will pass, still has problems with PEP8

## [0.5.12] - 2019-01-25

### Changed

- Don't try and compress whitespace in entity nodes

## [0.5.11] - 2019-01-01

### Added

- Add the info logging function for another output type
- Add option to surpress populating default attributes from the DTD

## [0.5.10] - 2018-09-02

### Changed

- The no xinclude option is expanded to include processing `<?rfc include=""?>` PI

## [0.5.6] - 2018-07-02

### Added

- Add option to not resolve entities for XML Linting

### Changed

- Fix problem with installing on a clean platform

## [0.5.5] - 2018-06-12

### Changed

- Correct problem with displaying utf8 strings

## [0.5.3] - 2018-04-01

### Changed

- Copy the cache code in for URLs on .dtd and .ent files, this allows for a DTD to be grabbed from the network
- Switch to using resolve_string in those cases where we have cached the file so that futher includes have the correct path when getting resolved.

## [0.5.2] - 2018-03-30

### Changed

- Distribute the old rfc 2629 dtd and ent files so that v2 files parse correctly
- Correct processing so that we can play games with where to search file files. If the file does not exist and the source directory is given then strip the path so that we will search in different directories for the file.

## [0.5.1] - 2018-03-01

### Added

- Setup to publish to PyPI

## [0.5.0] - 2018-02-25

### Changed

- Setup log routines so that UTF-8 strings can be written on all consoles.  This is a problem as Python v2 thinks consoles are written assumed to be ASCII and for Windows it is the code page of the console.  Pipes have a third method of making this decision
- Swap the order of two attributes to match the order in the xmlrfc v2 to v3 upgrade program.

## [0.0.3] - 2018-02-11

### Added

- Include RFC2629 DTD for the XMLDIFF so that we can load old xml files

### Changed

- For python 3.x read file as binary not text, deals with UTF-8 problems

## [0.0.2] - 2018-01-26

### Added

- Add additional parameter to logging functions
- Correct README.rst file, should be able to be released publicly

## [0.0.1] - 2018-01-05

### Added

- Create the initial simple version
- Create python setup program


[0.6.1]: https://github.com/ietf-tools/rfctools-common/compare/0.6.0...0.6.1
[0.6.0]: https://github.com/ietf-tools/rfctools-common/compare/0.5.17...0.6.0
[0.5.17]: https://github.com/ietf-tools/rfctools-common/compare/0.5.16...0.5.17
[0.5.16]: https://github.com/ietf-tools/rfctools-common/compare/0.5.15...0.5.16
[0.5.15]: https://github.com/ietf-tools/rfctools-common/compare/0.5.14...0.5.15
[0.5.14]: https://github.com/ietf-tools/rfctools-common/compare/0.5.12...0.5.14
[0.5.12]: https://github.com/ietf-tools/rfctools-common/compare/0.5.11...0.5.12
[0.5.11]: https://github.com/ietf-tools/rfctools-common/compare/0.5.10...0.5.11
[0.5.10]: https://github.com/ietf-tools/rfctools-common/compare/0.5.6...0.5.10
[0.5.6]: https://github.com/ietf-tools/rfctools-common/compare/0.5.5...0.5.6
[0.5.5]: https://github.com/ietf-tools/rfctools-common/compare/0.5.3...0.5.5
[0.5.3]: https://github.com/ietf-tools/rfctools-common/compare/0.5.2...0.5.3
[0.5.2]: https://github.com/ietf-tools/rfctools-common/compare/0.5.1...0.5.2
[0.5.1]: https://github.com/ietf-tools/rfctools-common/compare/0.5.0...0.5.1
[0.5.0]: https://github.com/ietf-tools/rfctools-common/compare/0.0.3...0.5.0
[0.0.3]: https://github.com/ietf-tools/rfctools-common/compare/0.0.2...0.0.3
[0.0.2]: https://github.com/ietf-tools/rfctools-common/compare/0.0.1...0.0.2
[0.0.1]: https://github.com/ietf-tools/rfctools-common/releases/tag/0.0.1
[v0.7.0]: https://github.com/ietf-tools/rfctools-common/compare/0.6.2...v0.7.0
