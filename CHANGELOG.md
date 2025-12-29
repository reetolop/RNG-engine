# 📜 Changelog

All notable changes to this project will be documented here.

## [v0.1.0] - 2025-12-30
### Added
- Core dice engine with class-based structure
- Session-wide statistics: total, average, median, mode
- Type annotations using `typing` module (`List`, `Union`, etc.)
- CLI integration for rolling and viewing stats
- `reset_stats()` method for fresh sessions

### Changed
- Refactored all session stats to use `@classmethod`s
- Cleaned up comments and clarified variable roles

### Notes
- Dice roller game updated to use new engine and temporary stats viewer (GUI overhaul coming soon!)
