# Lab 001 — Linux PATH Security

## Objective

Understand how the Linux `PATH` environment variable affects command execution
and how an unsafe directory in `PATH` can lead to command substitution.

## Environment

- OS: Kali Linux
- Shell: Zsh
- Project: BushidoForge-Lab

## Lab Structure

The laboratory contains:

- `labs/path-lab/fake/`
- `labs/path-lab/safe/`

Both directories contain an executable named `hello`.

## Commands Used

```bash
echo $PATH
which hello
type hello
command -v hello
```

## Experiment

A fake executable was placed in a directory that was added to the beginning
of the `PATH`.

The system then resolved `hello` to the executable located in that directory.

## Security Relevance

The order of directories in `PATH` affects which executable is selected when
the command is entered without an absolute path.

An attacker who can influence `PATH` or place a malicious executable in a
directory searched earlier may cause unintended code execution.

This is especially relevant when scripts or administrative processes execute
commands without absolute paths.

## Key Lesson

`PATH` is not just a convenience mechanism. It is part of the command
execution environment and can become a security boundary.

## Next Step

Investigate:

- `PATH` inheritance
- `sudo` and environment sanitization
- executable precedence
- absolute vs relative command paths
- secure configuration of administrative scripts
