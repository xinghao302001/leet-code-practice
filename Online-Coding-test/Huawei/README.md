## LRU
### 基本概念
- 核心思想：__最近最少使用的内容__ 最不可能在未来被使用，因此应优先淘汰。
当缓存空间满了，需要淘汰一些数据时，LRU 会选择最久没有被访问的数据进行移除。

### LRU的应用场景
- 操作系统内存管理：用来管理页的置换。
- 缓存系统：比如浏览器缓存、数据库缓存，存储经常被访问的数据。
- 虚拟内存：计算机通过 LRU 来决定要淘汰哪个页面。
- Web服务：管理常用请求的数据，提升访问性能。