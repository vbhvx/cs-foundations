# Computer Science Foundations & Systems Engineering Laboratory

A production-grade laboratory implementing foundational computer science abstractions, low-level concurrency primitives, operating systems scheduling, networking protocols, database storage engines, and distributed consensus algorithms.

## Repository Architecture

- **Foundations (`foundations/`)**: Bit manipulation, memory struct alignment, Gray codes, CRC32, FNV-1a, MurmurHash3, and variable-length quantities.
- **Concurrency (`concurrency/`)**: Spinlocks, counting semaphores, bounded queues, condition variables, reader-writer locks, thread pools, and deadlock detection.
- **Operating Systems (`os_internals/`)**: CPU scheduling (FCFS, SJF, RR, MLFQ), page replacement (FIFO, LRU, Clock, Optimal), TLB caches, two-level page tables, and inode filesystems.
- **Networking (`networking/`)**: Packet framing, streaming decoders, HTTP/1.1 request/response parsers, Token/Leaky bucket rate limiters, Go-Back-N sliding windows, and DNS encoding.
- **Storage Engines (`storage/`)**: Write-Ahead Log (WAL), in-memory SkipLists, immutable SSTables, two-way compaction, B-Trees, and an integrated LSM-tree key-value store.
- **Distributed Systems (`distributed/`)**: O(1) LRU and LFU caches, consistent hash rings with virtual nodes, Vector Clocks, Bloom filters, Merkle trees, and Raft consensus.

## Test Suite & Verification

Run the comprehensive test suite:
```bash
pytest tests/ -v
```
