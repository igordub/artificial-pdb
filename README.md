# Artificial PDB structures
Let's make non-existing PDB structures of any shape and for any taste.

## PDB file format

`ATOM` line in PDB file must look like:
```python
"{:6s}{:5d} {:^4s}{:1s}{:3s} {:1s}{:4d}{:1s}   {:8.3f}{:8.3f}{:8.3f}{:6.2f}{:6.2f}          {:>2s}{:2s}".format(...)
```

## References

- [PDB file format](https://cupnet.net/pdb-format/)
- [PDB to FASTA in Bash](https://cupnet.net/pdb2fasta/)