# hookpool_client_chia
Create a fair  just and automatic transfer mining pool for chia  
创建一个简单，快捷，爆块收益自动转账的chia矿池，目标就是一起愉快地挖矿
## 为什么选择hookpool
1.我们矿池采用实时转账的方式，也就是矿池检测到爆块就会自动计算矿工贡献值，程序自动完成收益分配工作  
  也就是无需提现申请，也杜绝了偷算力的可能，我们也提供我们的矿池钱包地址供矿友们监督： 
  我们矿池钱包地址：xch1azy95ut4we8n4afqk35637c6el3vrklhuhj2fclk7h6ads8r2w7q3j450j  
  可以用区块浏览网站查看矿池收益：  
  [矿池地址区块查看](https://www.chiaexplorer.com/blockchain/address/xch1azy95ut4we8n4afqk35637c6el3vrklhuhj2fclk7h6ads8r2w7q3j450j)  
2.我们矿池不做算力限制，最小转账单位是1mojo，也就是官方的最小转账单位（1mojo=亿万分之一XCH）  
3.下载打开客户端即可挖矿，我们挖矿软件使用官方api自动绑定当前的官方钱包    
  关于矿池的运作原理，以及为何我们不需要输入助记词，我们后续会用流程图解释下矿池运作原理  
  简而言之，我们矿池运作方式有点类似于官方矿池的运作方式，为了矿池的信任，我们会尽量解释清楚，甚至后续会开源一部分代码  
## 关于官方矿池和双挖看法
官方矿池的源码地址：https://github.com/Chia-Network/pool-reference  
功能感觉跟我们的差不多，而且有官方优势，但是我们有以下优点： 
1.官方矿池同样需要你同步完节点后才能挖矿，我们矿池采用服务器分配任务方式挖矿，因此hookpool不需要矿工每台电脑都同步节点完才能挖矿，用过chia的都受过同步节点的苦  
2.查看了官方矿池代码进度，有点猴年马月的感觉 因此，我们还是开放了我们的矿池，给现有的矿池减轻压力  
3.对于双挖，从chia源码分析的角度，无法避免，但是我们不提倡双挖  
  特别对于小算力的矿友，假设你选择我们矿池和hpool之间双挖，chia爆块几率是一样的，区别在于我们矿池和hpool各自提交proof（证据）的速度  
  如果我们抢不过hpool，你就算在hpool有些许收益，但是想达到0.2XCH的提现门槛很难，后续hpool算力计算提升就更难（现在2T以下不计算收益了）  
  你提现不了同时我们矿池也没有爆块收益实时分配，那还不是两头空  
  无论双挖，还是n挖，对于单个用户的爆块几率是一样的

## 进度
1.创建一个挖矿客户端：初步完成  
2.正测试chia转账功能，我们已经完成了矿池的收益自动转账功能，转账的快慢取决于节点同步的速度，我们转账没有给fee（小费），所以同步会慢一些，但是自动转账功能是好用的，而且最小单位是mojo（万亿分之一的XCH） 
3.矿池全部功能已经完成，现在推出公测  
## chia pool 矿池功能
1.矿池的挖矿程序运行需要在安装有官方钱包的机子上，我们使用官方api和官方钱包关联 
2.我们不提供需要输入助记词绑定的工具 
3.挖矿工具实时显示收益，矿池的收益一分钟轮询一次，矿池爆块收益的话会触发自动转账功能，把收益按照贡献值分配给矿工  
4.我们设计了空投发红包功能，设定了矿池钱包地址收益小于1XCH的时候，会触发发红包给矿池所有的矿工  
5.我们会逐步公开挖矿代码和收益分配的代码，让矿友们放心使用  
6.转账的最小单位是1mojo,这个是官方转账的最小单位（亿万分之一XCH），没法再小了
## chia pool的空投发红包
1.我们设计了发红包环节，主要是矿池起步阶段，算力不够，爆块时间不确定  
2.因此我们设计了空投矿池钱包地址，然后矿池钱包自动检测到有收益，按照类似微信红包分配原则，分配给矿池的矿友们  
3.这个功能同时也测试了矿池检测到收益自动转账  
4.欢迎各位矿友加入到空投发红包环节，给矿池的矿友发红包  
5.矿池的空投钱包地址：  
xch1azy95ut4we8n4afqk35637c6el3vrklhuhj2fclk7h6ads8r2w7q3j450j  
6.欢迎空投这个矿池地址给矿友们发红包，空投不要超过1XCH，不然会触发爆块按算力分配收益，不超过1XCH的空投，则会按照微信红包的规则随机分配收益给矿友

## 上线公测环节
欢迎各位矿友加入到矿池一起愉快的挖矿
## 关于矿池收益
我们提供统一服务器分配任务挖矿，因此有一定的成本，为了能维持下去，我们每次爆块转账时候会收取千分之五的手续费  
矿池钱包截留1001mojozuo为之后可能要付转账手续费做准备，其余的费用一分都不会收取，每次爆块都第一时间自动分配收益  
## 关于矿友如何查看收益
1.通过官方钱包查看收益（需要同步钱包高度，不然看不到收益）
2.通过区块浏览器查看：https://www.chiaexplorer.com/blockchain/address/+钱包地址
## 关于转账时间
目前我们实际测试，一笔交易等待节点确认时间需要30s以上，然后官方暂时没有多地址单次交易的api（官方矿池有send_transaction_multi，但是没有开源出来）  
也就是说一天处理的交易：
`24*60*2=2880笔`
一天的极限交易也就这么多笔，等官方添加了新API我们会同步过来
but  
5月25号，经过一整晚上的撸源码，我们找到了解决方案，可以不用受一天2880笔转账的限制，可以愉快的玩耍了
