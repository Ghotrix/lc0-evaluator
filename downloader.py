from bs4 import BeautifulSoup
import subprocess

html_data = '''<table class="table table-striped table-sm">
    <tbody>
      
      <tr>
        <td>342</td>
        <td><a href="/get_network?sha=cb54812a032e54a5026b07b94721e940bb0bbaa2b7fe493524e147bfdb4f36fb" download="weights_342.txt.gz">cb54812a</a></td>
        <td>5917.83</td>
        <td>35300</td>
        <td>15</td>
        <td>192</td>
        <td>2018-05-26 05:18:06.197604 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>341</td>
        <td><a href="/get_network?sha=7899cea74e343ef5bad02bccbfdd371b82fc9630b91fb4d50c4656becefc9092" download="weights_341.txt.gz">7899cea7</a></td>
        <td>5891.74</td>
        <td>39360</td>
        <td>15</td>
        <td>192</td>
        <td>2018-05-25 23:52:39.496824 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>340</td>
        <td><a href="/get_network?sha=f4f6954e4e3838a331e9e9270b24d39a465d03a5846067f457500c7d4bee47b8" download="weights_340.txt.gz">f4f6954e</a></td>
        <td>5897.06</td>
        <td>39502</td>
        <td>15</td>
        <td>192</td>
        <td>2018-05-25 18:17:59.990353 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>339</td>
        <td><a href="/get_network?sha=f3e926e9b698dcfcfccd6a89a5298c23f335a304a548b0719c7810f6bab49c1a" download="weights_339.txt.gz">f3e926e9</a></td>
        <td>5893.88</td>
        <td>42443</td>
        <td>15</td>
        <td>192</td>
        <td>2018-05-25 12:48:09.759265 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>338</td>
        <td><a href="/get_network?sha=597ba6dce46e250fbbef334cf561581581292c680c3313bc65fd80579e67af46" download="weights_338.txt.gz">597ba6dc</a></td>
        <td>5910.15</td>
        <td>37972</td>
        <td>15</td>
        <td>192</td>
        <td>2018-05-25 07:45:52.242816 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>337</td>
        <td><a href="/get_network?sha=c197a634698ee97b7673cc8f1b8a0bb1897b24e15ed26129875b326b57d4f1e8" download="weights_337.txt.gz">c197a634</a></td>
        <td>5891.58</td>
        <td>41797</td>
        <td>15</td>
        <td>192</td>
        <td>2018-05-25 01:51:02.347094 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>336</td>
        <td><a href="/get_network?sha=7c2d247d68b40860ea6849117e4954a3e87be598c48d8b803315e7cfeb304721" download="weights_336.txt.gz">7c2d247d</a></td>
        <td>5887.60</td>
        <td>39658</td>
        <td>15</td>
        <td>192</td>
        <td>2018-05-24 19:48:33.616708 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>335</td>
        <td><a href="/get_network?sha=5d46d9c438a6901e7cd8ebfde15ec00117119cabfcd528d4ce5f568243ded5ee" download="weights_335.txt.gz">5d46d9c4</a></td>
        <td>5902.26</td>
        <td>36612</td>
        <td>15</td>
        <td>192</td>
        <td>2018-05-24 14:52:01.490785 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>334</td>
        <td><a href="/get_network?sha=1d80f609383b4494455f28527ca401949bdf4cfc7cca0fe8c82394d6b8152fbf" download="weights_334.txt.gz">1d80f609</a></td>
        <td>5890.82</td>
        <td>34512</td>
        <td>15</td>
        <td>192</td>
        <td>2018-05-24 10:19:05.793444 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>333</td>
        <td><a href="/get_network?sha=ba31cd9d4bc0ef02d6ff7db8135e90a0bfba97227ee47f77c468cea85090a33f" download="weights_333.txt.gz">ba31cd9d</a></td>
        <td>5897.34</td>
        <td>46395</td>
        <td>15</td>
        <td>192</td>
        <td>2018-05-24 04:18:19.198303 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>332</td>
        <td><a href="/get_network?sha=d452b6491ff286b236023947fb8579b42c51e3e4db003e5dfa8c9fc03066eaa2" download="weights_332.txt.gz">d452b649</a></td>
        <td>5876.13</td>
        <td>12041</td>
        <td>15</td>
        <td>192</td>
        <td>2018-05-24 02:33:26.766309 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>331</td>
        <td><a href="/get_network?sha=49f2152bc5f325cfe776fbb26bd9994c2bd1589e0e7bbd3486d64e18bb7b2383" download="weights_331.txt.gz">49f2152b</a></td>
        <td>5900.69</td>
        <td>62170</td>
        <td>15</td>
        <td>192</td>
        <td>2018-05-23 17:50:09.509944 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>330</td>
        <td><a href="/get_network?sha=de60388a796954c56b4f871d689741bd9274598f07c14c9db9313ea918ba4821" download="weights_330.txt.gz">de60388a</a></td>
        <td>5905.68</td>
        <td>68274</td>
        <td>15</td>
        <td>192</td>
        <td>2018-05-23 09:43:14.535737 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>329</td>
        <td><a href="/get_network?sha=1831f4884d6da86fe369d4a51fbfe6a433703fbf97b0e7122898170c1eede5e0" download="weights_329.txt.gz">1831f488</a></td>
        <td>5888.86</td>
        <td>205952</td>
        <td>15</td>
        <td>192</td>
        <td>2018-05-22 07:31:19.895557 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>328</td>
        <td><a href="/get_network?sha=a7b32f2b83ccb494595c52d0e673f34b3eeab815125cdcc36e77115518391909" download="weights_328.txt.gz">a7b32f2b</a></td>
        <td>5883.91</td>
        <td>34640</td>
        <td>15</td>
        <td>192</td>
        <td>2018-05-22 02:20:04.900609 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>327</td>
        <td><a href="/get_network?sha=acfed70d789546b3ea6c5f3aa35d24a6abc108752a123217a033a48ec671eb98" download="weights_327.txt.gz">acfed70d</a></td>
        <td>5877.68</td>
        <td>31511</td>
        <td>15</td>
        <td>192</td>
        <td>2018-05-21 21:15:40.320972 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>326</td>
        <td><a href="/get_network?sha=a1beb99d301fa949624252c1a78b7997996e3d5a246060f8c1a23689817b7572" download="weights_326.txt.gz">a1beb99d</a></td>
        <td>5877.68</td>
        <td>33009</td>
        <td>15</td>
        <td>192</td>
        <td>2018-05-21 15:58:12.83613 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>325</td>
        <td><a href="/get_network?sha=07f8bb56d55c930970b2c426d9281a9385d1c132e537cb0c272a3527b67069c9" download="weights_325.txt.gz">07f8bb56</a></td>
        <td>5881.56</td>
        <td>34897</td>
        <td>15</td>
        <td>192</td>
        <td>2018-05-21 11:02:15.63419 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>324</td>
        <td><a href="/get_network?sha=ec0d0cf94bab8170e10b165219951fe0294153dd9adae68cb45fef328d3fa8c0" download="weights_324.txt.gz">ec0d0cf9</a></td>
        <td>5881.56</td>
        <td>35296</td>
        <td>15</td>
        <td>192</td>
        <td>2018-05-21 06:01:21.28207 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>323</td>
        <td><a href="/get_network?sha=a4fa64c64ced1d5557e95de049f4745ea53421ebe4849365b49bfcbb990fbcc5" download="weights_323.txt.gz">a4fa64c6</a></td>
        <td>5892.71</td>
        <td>31369</td>
        <td>15</td>
        <td>192</td>
        <td>2018-05-21 00:57:18.01188 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>322</td>
        <td><a href="/get_network?sha=4548fcf1099d9a10f537b32be6fa1307a742d2eac4e16a6e30ebee959beea7b8" download="weights_322.txt.gz">4548fcf1</a></td>
        <td>5878.43</td>
        <td>32010</td>
        <td>15</td>
        <td>192</td>
        <td>2018-05-20 19:26:54.997148 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>321</td>
        <td><a href="/get_network?sha=37e84ab7016152dd7ddbd7414adc81f96639209d3d36c0c2c7575b4eb4a0b219" download="weights_321.txt.gz">37e84ab7</a></td>
        <td>5856.51</td>
        <td>32287</td>
        <td>15</td>
        <td>192</td>
        <td>2018-05-20 14:20:49.838468 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>320</td>
        <td><a href="/get_network?sha=bb734c5fb1ce927079b8a831890d972faf2a1c5eb99d632cbbdc814080308a2b" download="weights_320.txt.gz">bb734c5f</a></td>
        <td>5842.79</td>
        <td>33618</td>
        <td>15</td>
        <td>192</td>
        <td>2018-05-20 09:09:34.857183 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>319</td>
        <td><a href="/get_network?sha=7af1426354a4041cf236aee496025d51c5f6b0176091d256ba8e1ea2e8358a6b" download="weights_319.txt.gz">7af14263</a></td>
        <td>5821.74</td>
        <td>33478</td>
        <td>15</td>
        <td>192</td>
        <td>2018-05-20 04:16:45.546583 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>318</td>
        <td><a href="/get_network?sha=b75a5490f53448e9e82e540e67eb825544f8521c7a6f20bed4af43f9beb072df" download="weights_318.txt.gz">b75a5490</a></td>
        <td>5812.70</td>
        <td>28971</td>
        <td>15</td>
        <td>192</td>
        <td>2018-05-19 23:34:10.700899 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>317</td>
        <td><a href="/get_network?sha=514560016e28bb9cf5c7d134fb6ef25cf9e1fca30cfb9f117eae1d23a9f48ff5" download="weights_317.txt.gz">51456001</a></td>
        <td>5812.70</td>
        <td>31718</td>
        <td>15</td>
        <td>192</td>
        <td>2018-05-19 18:21:52.402873 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>316</td>
        <td><a href="/get_network?sha=5d78d435aaab428f347893afcf1c47a9ab45b67531b0d72d466f59b7b9574312" download="weights_316.txt.gz">5d78d435</a></td>
        <td>5802.47</td>
        <td>31878</td>
        <td>15</td>
        <td>192</td>
        <td>2018-05-19 13:30:31.36175 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>315</td>
        <td><a href="/get_network?sha=a263c645305f324534b46168d004461934f6069aca92d332937573a881954ecf" download="weights_315.txt.gz">a263c645</a></td>
        <td>5784.58</td>
        <td>35363</td>
        <td>15</td>
        <td>192</td>
        <td>2018-05-19 08:29:33.767935 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>314</td>
        <td><a href="/get_network?sha=0cb9b8728eb80115a68f6dd8415aca2365b994c41483e826f7c199cd62592a77" download="weights_314.txt.gz">0cb9b872</a></td>
        <td>5785.53</td>
        <td>33730</td>
        <td>15</td>
        <td>192</td>
        <td>2018-05-19 03:38:43.667917 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>313</td>
        <td><a href="/get_network?sha=8f18bc497cdce2b26bb38f27f064579c65e26d3188fda31bf78625449e967814" download="weights_313.txt.gz">8f18bc49</a></td>
        <td>5765.19</td>
        <td>31555</td>
        <td>15</td>
        <td>192</td>
        <td>2018-05-18 22:45:09.104962 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>312</td>
        <td><a href="/get_network?sha=17c947acf32c599b9af0f25d4f2da36d7ae864e6dd7bf33cf73cacb10bd22a25" download="weights_312.txt.gz">17c947ac</a></td>
        <td>5778.69</td>
        <td>34827</td>
        <td>15</td>
        <td>192</td>
        <td>2018-05-18 17:27:58.534047 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>311</td>
        <td><a href="/get_network?sha=87eb9e6c67e404af02c79324a0bdb76864b456a914e50f79f4e09fdeed8d4f42" download="weights_311.txt.gz">87eb9e6c</a></td>
        <td>5771.79</td>
        <td>34957</td>
        <td>15</td>
        <td>192</td>
        <td>2018-05-18 12:29:02.479044 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>310</td>
        <td><a href="/get_network?sha=665e0605be59e20d0d0019313f734f2d650fbe89cf6241270de3da61f8fcf02a" download="weights_310.txt.gz">665e0605</a></td>
        <td>5768.99</td>
        <td>35223</td>
        <td>15</td>
        <td>192</td>
        <td>2018-05-18 07:36:36.505138 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>309</td>
        <td><a href="/get_network?sha=828a487307d1e3185328c77ac443d599bba491a4721f43803df0be5e3a61d377" download="weights_309.txt.gz">828a4873</a></td>
        <td>5749.83</td>
        <td>36150</td>
        <td>15</td>
        <td>192</td>
        <td>2018-05-18 02:35:50.0973 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>308</td>
        <td><a href="/get_network?sha=93be75e53dd96929b2badc80375e3444ab2ae039213fbe88c57a8b15c40968d9" download="weights_308.txt.gz">93be75e5</a></td>
        <td>5757.48</td>
        <td>33253</td>
        <td>15</td>
        <td>192</td>
        <td>2018-05-17 21:35:53.420456 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>307</td>
        <td><a href="/get_network?sha=c17b9557f017fd3ac0046a81077c8b289ba6181acb10af1082a0374e9cb59b48" download="weights_307.txt.gz">c17b9557</a></td>
        <td>5737.44</td>
        <td>32760</td>
        <td>15</td>
        <td>192</td>
        <td>2018-05-17 16:40:29.821554 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>306</td>
        <td><a href="/get_network?sha=2c436121e4d3c30668c9a4b8ee7727319d7d9836387f9c4d600a00395de3c39a" download="weights_306.txt.gz">2c436121</a></td>
        <td>5731.56</td>
        <td>35972</td>
        <td>15</td>
        <td>192</td>
        <td>2018-05-17 11:29:07.361052 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>305</td>
        <td><a href="/get_network?sha=cc46dcd2e730a3a9a4196b3fe1bad9ac477f25d6abb3f72451d1e4180534013d" download="weights_305.txt.gz">cc46dcd2</a></td>
        <td>5729.60</td>
        <td>33542</td>
        <td>15</td>
        <td>192</td>
        <td>2018-05-17 06:32:22.557845 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>304</td>
        <td><a href="/get_network?sha=c5cdc90230b35c43d23bf5867e75ff65af06b81b57e8900f2ef0449d99a19814" download="weights_304.txt.gz">c5cdc902</a></td>
        <td>5699.67</td>
        <td>32672</td>
        <td>15</td>
        <td>192</td>
        <td>2018-05-17 01:38:06.512582 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>303</td>
        <td><a href="/get_network?sha=2c6fb5fa5888d704dcae64dbcdf7df5afc77de74c739ed987ad799c868caf164" download="weights_303.txt.gz">2c6fb5fa</a></td>
        <td>5710.94</td>
        <td>33237</td>
        <td>15</td>
        <td>192</td>
        <td>2018-05-16 20:40:21.131276 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>302</td>
        <td><a href="/get_network?sha=ade7ac458b440ca3d5759e9f4a3e8fd38e988ee8c7e0c8701f211ad855c36f46" download="weights_302.txt.gz">ade7ac45</a></td>
        <td>5699.27</td>
        <td>33980</td>
        <td>15</td>
        <td>192</td>
        <td>2018-05-16 15:44:28.099164 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>301</td>
        <td><a href="/get_network?sha=c1ec1426b96927d921ca69e78b3b73cebdb7bc69b29ee6cfc678b62d1840ad12" download="weights_301.txt.gz">c1ec1426</a></td>
        <td>5664.37</td>
        <td>37597</td>
        <td>15</td>
        <td>192</td>
        <td>2018-05-16 10:48:47.694156 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>300</td>
        <td><a href="/get_network?sha=6fb42b3d98ada791f2d27b51b7dc65c62f360b005400a0a88ad48623142f195b" download="weights_300.txt.gz">6fb42b3d</a></td>
        <td>5666.69</td>
        <td>36391</td>
        <td>15</td>
        <td>192</td>
        <td>2018-05-16 05:52:12.495146 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>299</td>
        <td><a href="/get_network?sha=705132aeb89a8a3a71226bd56f1af8a08b97344c353bab4ed5e015a70b8512ec" download="weights_299.txt.gz">705132ae</a></td>
        <td>5647.77</td>
        <td>32010</td>
        <td>15</td>
        <td>192</td>
        <td>2018-05-16 00:57:29.303565 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>298</td>
        <td><a href="/get_network?sha=2ff806dd7ecb6fe80a27780ba5b334eb804b091a73ae0958a5aee2ab7bce79cc" download="weights_298.txt.gz">2ff806dd</a></td>
        <td>5640.69</td>
        <td>13356</td>
        <td>15</td>
        <td>192</td>
        <td>2018-05-15 22:49:13.765667 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>297</td>
        <td><a href="/get_network?sha=2b97eb02a7bb19f7edb323ac7641e7cf0b0b89c203c2c93d5facba1a12611f65" download="weights_297.txt.gz">2b97eb02</a></td>
        <td>5633.78</td>
        <td>51949</td>
        <td>15</td>
        <td>192</td>
        <td>2018-05-15 15:02:19.452642 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>296</td>
        <td><a href="/get_network?sha=afd5b5a58ed79f806dd93ba135ba2f417e4ca43c56655c1c3fff2bd532b4e03f" download="weights_296.txt.gz">afd5b5a5</a></td>
        <td>5616.58</td>
        <td>32755</td>
        <td>15</td>
        <td>192</td>
        <td>2018-05-15 10:07:16.212104 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>295</td>
        <td><a href="/get_network?sha=7506325fd50d30540ac15c9898d6ca9d1eefd2ee1db5fa644a7cdc39f1894f12" download="weights_295.txt.gz">7506325f</a></td>
        <td>5599.31</td>
        <td>32397</td>
        <td>15</td>
        <td>192</td>
        <td>2018-05-15 05:14:04.21092 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>294</td>
        <td><a href="/get_network?sha=060569a71a2c8fed39276d6eab4619df06cc734ebd11742deb1eefc5c5876b3e" download="weights_294.txt.gz">060569a7</a></td>
        <td>5593.65</td>
        <td>31949</td>
        <td>15</td>
        <td>192</td>
        <td>2018-05-15 00:14:39.91945 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>293</td>
        <td><a href="/get_network?sha=65aff04f6e33f05799d0cbb0fe5aa23ae07ac8f969a0d2d6d0b58416c0e6f5da" download="weights_293.txt.gz">65aff04f</a></td>
        <td>5593.65</td>
        <td>32561</td>
        <td>15</td>
        <td>192</td>
        <td>2018-05-14 19:21:25.513033 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>292</td>
        <td><a href="/get_network?sha=feb55804b360dcc863b18383142607bf3284b26b92d45e2c29e2805e83cc659c" download="weights_292.txt.gz">feb55804</a></td>
        <td>5572.43</td>
        <td>33646</td>
        <td>15</td>
        <td>192</td>
        <td>2018-05-14 14:24:00.795271 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>291</td>
        <td><a href="/get_network?sha=f9dccd450a1ecf143bb538b61b4c826dbf30d3d966cd7be615884ba20083dfe3" download="weights_291.txt.gz">f9dccd45</a></td>
        <td>5549.95</td>
        <td>32735</td>
        <td>15</td>
        <td>192</td>
        <td>2018-05-14 09:25:17.887024 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>290</td>
        <td><a href="/get_network?sha=e5871d8cc59c86b76ca6a210dd0134842602a734846ddef2da3862b924b34a32" download="weights_290.txt.gz">e5871d8c</a></td>
        <td>5547.54</td>
        <td>32732</td>
        <td>15</td>
        <td>192</td>
        <td>2018-05-14 04:28:21.099604 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>289</td>
        <td><a href="/get_network?sha=ac8745cc390486cedec85b49874c607e0cc8c6c9c05800fc19dd72fae770b769" download="weights_289.txt.gz">ac8745cc</a></td>
        <td>5533.62</td>
        <td>28918</td>
        <td>15</td>
        <td>192</td>
        <td>2018-05-13 23:38:07.535652 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>288</td>
        <td><a href="/get_network?sha=eb937f9dd237b4878cb9183b6cdda2319e8b15c799cd4c6f352697b52d336151" download="weights_288.txt.gz">eb937f9d</a></td>
        <td>5519.79</td>
        <td>32963</td>
        <td>15</td>
        <td>192</td>
        <td>2018-05-13 18:29:13.336384 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>287</td>
        <td><a href="/get_network?sha=2e0daa3695e2c8db27ef6c3fb0984b6764de8549045cdf706530ea2b7c2c312e" download="weights_287.txt.gz">2e0daa36</a></td>
        <td>5492.49</td>
        <td>32164</td>
        <td>15</td>
        <td>192</td>
        <td>2018-05-13 13:23:41.61204 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>286</td>
        <td><a href="/get_network?sha=493148cd7a10c5f9861f63facfc5aa395cc555af8543766de5bc6fca39405232" download="weights_286.txt.gz">493148cd</a></td>
        <td>5443.92</td>
        <td>31678</td>
        <td>15</td>
        <td>192</td>
        <td>2018-05-13 08:16:50.702799 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>285</td>
        <td><a href="/get_network?sha=1be7743624b1c2f3459af2f0ca1961256368db377c1600cfeb4ad4c743dbabd5" download="weights_285.txt.gz">1be77436</a></td>
        <td>5462.64</td>
        <td>31727</td>
        <td>15</td>
        <td>192</td>
        <td>2018-05-13 03:19:44.22148 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>284</td>
        <td><a href="/get_network?sha=ebcec73e28cd12de80b203e76a0dccf2d77b88b763552ff61233633113c1e4d8" download="weights_284.txt.gz">ebcec73e</a></td>
        <td>5478.62</td>
        <td>29016</td>
        <td>15</td>
        <td>192</td>
        <td>2018-05-12 22:26:00.131638 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>283</td>
        <td><a href="/get_network?sha=fe7638fbe4c6dd4d2aac9bb78e1b9471eceabd75f651ec816e4707cfb9707dd3" download="weights_283.txt.gz">fe7638fb</a></td>
        <td>5459.46</td>
        <td>31173</td>
        <td>15</td>
        <td>192</td>
        <td>2018-05-12 17:28:31.665599 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>282</td>
        <td><a href="/get_network?sha=dc26901404ef033c82f79b590addbf0dcbe061cd74d2ba967510917b06c3928c" download="weights_282.txt.gz">dc269014</a></td>
        <td>5484.82</td>
        <td>30961</td>
        <td>15</td>
        <td>192</td>
        <td>2018-05-12 12:31:25.070883 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>281</td>
        <td><a href="/get_network?sha=54e8b76afe981950c24d744e8c56f1df6a6c165b28410a7c1d1b08ba67501bd1" download="weights_281.txt.gz">54e8b76a</a></td>
        <td>5508.24</td>
        <td>33766</td>
        <td>15</td>
        <td>192</td>
        <td>2018-05-12 07:32:27.950466 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>280</td>
        <td><a href="/get_network?sha=ca578e364938552c3fdbccc0aab268cc0b2f3c44a26d6d3422f16640e1aa8ece" download="weights_280.txt.gz">ca578e36</a></td>
        <td>5512.02</td>
        <td>32731</td>
        <td>15</td>
        <td>192</td>
        <td>2018-05-12 02:34:27.823094 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>279</td>
        <td><a href="/get_network?sha=91f1259abc775649b206e9351b86d7a356d21cfe8382e7ec83cd3447419c94bd" download="weights_279.txt.gz">91f1259a</a></td>
        <td>5506.77</td>
        <td>31812</td>
        <td>15</td>
        <td>192</td>
        <td>2018-05-11 21:33:34.884911 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>278</td>
        <td><a href="/get_network?sha=3e0b9186217dff4e55f810bf40065ccac08ab8dd8c56cdc054cc00056d48e6fb" download="weights_278.txt.gz">3e0b9186</a></td>
        <td>5503.05</td>
        <td>35771</td>
        <td>15</td>
        <td>192</td>
        <td>2018-05-11 15:57:08.563026 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>277</td>
        <td><a href="/get_network?sha=c61a0a8a2c0767f0129ee910a1e178ee60bee095da6fd066fcfa8c610291fad4" download="weights_277.txt.gz">c61a0a8a</a></td>
        <td>5570.47</td>
        <td>37828</td>
        <td>15</td>
        <td>192</td>
        <td>2018-05-11 11:03:04.29938 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>276</td>
        <td><a href="/get_network?sha=438acf0e0ee1b5c2a90778288f777162d3ee663342bfd5c48512e6a9166aac77" download="weights_276.txt.gz">438acf0e</a></td>
        <td>5489.06</td>
        <td>32687</td>
        <td>15</td>
        <td>192</td>
        <td>2018-05-11 06:09:27.294094 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>275</td>
        <td><a href="/get_network?sha=8aad12cff4df9e79c2ed90bebbf4a37ab68e279994ad056c76176446fd680c3e" download="weights_275.txt.gz">8aad12cf</a></td>
        <td>5505.95</td>
        <td>29276</td>
        <td>15</td>
        <td>192</td>
        <td>2018-05-11 01:19:23.204603 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>274</td>
        <td><a href="/get_network?sha=30264a665fbf0ce618cb5edd06a1ce1311e0f1c8aa4564eb7135406ea0154dba" download="weights_274.txt.gz">30264a66</a></td>
        <td>5546.39</td>
        <td>30723</td>
        <td>15</td>
        <td>192</td>
        <td>2018-05-10 20:24:11.441951 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>273</td>
        <td><a href="/get_network?sha=dd22f583428a6be7129791860f0de4a7e026c82e91632d4a69ee56614915d3c6" download="weights_273.txt.gz">dd22f583</a></td>
        <td>5541.07</td>
        <td>34978</td>
        <td>15</td>
        <td>192</td>
        <td>2018-05-10 15:25:36.373958 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>272</td>
        <td><a href="/get_network?sha=3be7e173fe7fbd36af9382dc44d5887fc7703115553de3389e6fd737851c86ae" download="weights_272.txt.gz">3be7e173</a></td>
        <td>5534.36</td>
        <td>37262</td>
        <td>15</td>
        <td>192</td>
        <td>2018-05-10 10:31:42.351328 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>271</td>
        <td><a href="/get_network?sha=784068b0522aafa0070a9590a3d73d2782f37acb58566df24f99f0be64c5c2d7" download="weights_271.txt.gz">784068b0</a></td>
        <td>5565.23</td>
        <td>39710</td>
        <td>15</td>
        <td>192</td>
        <td>2018-05-10 05:32:56.598829 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>270</td>
        <td><a href="/get_network?sha=5b3638056a0592ded3ed02596ee477bc8009debae15a0acd8b95d41e4738e368" download="weights_270.txt.gz">5b363805</a></td>
        <td>5563.32</td>
        <td>34896</td>
        <td>15</td>
        <td>192</td>
        <td>2018-05-10 00:40:39.196697 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>269</td>
        <td><a href="/get_network?sha=c5a950212cbb40829c7c0b511bf06178a421fe84b61d26c17c786004036f77ce" download="weights_269.txt.gz">c5a95021</a></td>
        <td>5535.91</td>
        <td>36372</td>
        <td>15</td>
        <td>192</td>
        <td>2018-05-09 19:43:35.564943 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>268</td>
        <td><a href="/get_network?sha=8e37ed7c1a25731c9f24a33eae544357e296fd7854f19ea7ecc7b23702347b98" download="weights_268.txt.gz">8e37ed7c</a></td>
        <td>5582.06</td>
        <td>39317</td>
        <td>15</td>
        <td>192</td>
        <td>2018-05-09 14:48:43.353356 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>267</td>
        <td><a href="/get_network?sha=909b25303dd62ac65e7b52e2837870930df75e7e56aa7abeea8dc29e010904dc" download="weights_267.txt.gz">909b2530</a></td>
        <td>5564.21</td>
        <td>37873</td>
        <td>15</td>
        <td>192</td>
        <td>2018-05-09 09:50:16.795241 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>266</td>
        <td><a href="/get_network?sha=4c92ddb36e22742274b52b4b68731d6ca147ff9664e8952e7086cce65887be36" download="weights_266.txt.gz">4c92ddb3</a></td>
        <td>5592.64</td>
        <td>34453</td>
        <td>15</td>
        <td>192</td>
        <td>2018-05-09 04:54:12.561581 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>265</td>
        <td><a href="/get_network?sha=12f2afa50ace64f4f683f923de79cfb155986a4b4e678fa54b1b1f4d552fc42d" download="weights_265.txt.gz">12f2afa5</a></td>
        <td>5554.58</td>
        <td>33120</td>
        <td>15</td>
        <td>192</td>
        <td>2018-05-09 00:04:51.819759 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>264</td>
        <td><a href="/get_network?sha=d3d2a8b33b0e12856c7c4b5373cd485c573b9caadd9167f7f402c4adf5fff74e" download="weights_264.txt.gz">d3d2a8b3</a></td>
        <td>5579.41</td>
        <td>39053</td>
        <td>15</td>
        <td>192</td>
        <td>2018-05-08 19:10:26.107387 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>263</td>
        <td><a href="/get_network?sha=fcb425e2d844fecb7ffcb2db465c49def94fd14644a34791b1a3a4a722a1cf52" download="weights_263.txt.gz">fcb425e2</a></td>
        <td>5609.13</td>
        <td>41924</td>
        <td>15</td>
        <td>192</td>
        <td>2018-05-08 14:11:29.775667 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>262</td>
        <td><a href="/get_network?sha=891f63a9fe1f054441ee177d18b7626bb818ea9b9967c3db85bd6a0bbfa8f2e1" download="weights_262.txt.gz">891f63a9</a></td>
        <td>5610.01</td>
        <td>38388</td>
        <td>15</td>
        <td>192</td>
        <td>2018-05-08 09:29:38.641991 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>261</td>
        <td><a href="/get_network?sha=cf17d7dd1d22f140a7bf8fbef4c01ed2734fa29b9b3b6a16efd8fc584324513f" download="weights_261.txt.gz">cf17d7dd</a></td>
        <td>5593.02</td>
        <td>81832</td>
        <td>15</td>
        <td>192</td>
        <td>2018-05-07 22:55:17.245027 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>260</td>
        <td><a href="/get_network?sha=d906c1329275fd16430cf4272b31f95c9bf432312d6ba53ee3f47e612fb14e37" download="weights_260.txt.gz">d906c132</a></td>
        <td>5594.48</td>
        <td>39974</td>
        <td>15</td>
        <td>192</td>
        <td>2018-05-07 18:00:41.138898 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>259</td>
        <td><a href="/get_network?sha=d1869e2c2c5a1eac44c278f3e54f3f82f89f8821d8ec3e78e47ebb53d45e8e28" download="weights_259.txt.gz">d1869e2c</a></td>
        <td>5589.62</td>
        <td>44099</td>
        <td>15</td>
        <td>192</td>
        <td>2018-05-07 13:07:06.336413 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>258</td>
        <td><a href="/get_network?sha=fb4d42f88b67c2c02d0f885d175dbd9330c19cdc1f0d75718a7a6f62f787ba38" download="weights_258.txt.gz">fb4d42f8</a></td>
        <td>5601.41</td>
        <td>40543</td>
        <td>15</td>
        <td>192</td>
        <td>2018-05-07 08:07:38.949692 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>257</td>
        <td><a href="/get_network?sha=1efdf2a8461fe8fb5f4c86d152027fdd205e6eb3d6c0213b608f6c94d7a6176b" download="weights_257.txt.gz">1efdf2a8</a></td>
        <td>5595.92</td>
        <td>35852</td>
        <td>15</td>
        <td>192</td>
        <td>2018-05-07 03:15:52.151435 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>256</td>
        <td><a href="/get_network?sha=a58101db9d9fbd4122909c6138cb60c336b9ca3ddfb1e9136cee599d21a8fd62" download="weights_256.txt.gz">a58101db</a></td>
        <td>5605.43</td>
        <td>38396</td>
        <td>15</td>
        <td>192</td>
        <td>2018-05-06 22:13:48.301395 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>255</td>
        <td><a href="/get_network?sha=3a48d0f30fbb9afc181ec2ee16d8a6f8e2d88f2f1211838ff58cc0631f0869a6" download="weights_255.txt.gz">3a48d0f3</a></td>
        <td>5625.56</td>
        <td>39461</td>
        <td>15</td>
        <td>192</td>
        <td>2018-05-06 17:18:39.24005 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>254</td>
        <td><a href="/get_network?sha=749d168fbe89f82a0f994b0d594fbe725622f18b2546a450c475ced4fe5d44d3" download="weights_254.txt.gz">749d168f</a></td>
        <td>5639.16</td>
        <td>44103</td>
        <td>15</td>
        <td>192</td>
        <td>2018-05-06 12:17:47.105678 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>253</td>
        <td><a href="/get_network?sha=442d9a804063c606f4bcaa71dd58a04d065eb47642b3e59c512fdabbbbed376c" download="weights_253.txt.gz">442d9a80</a></td>
        <td>5641.39</td>
        <td>40349</td>
        <td>15</td>
        <td>192</td>
        <td>2018-05-06 07:21:22.684396 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>252</td>
        <td><a href="/get_network?sha=baa3fdd63a4ee38bffeecf6bf64c28a98a48ac36844edf9819b6b6285475e285" download="weights_252.txt.gz">baa3fdd6</a></td>
        <td>5625.36</td>
        <td>42540</td>
        <td>15</td>
        <td>192</td>
        <td>2018-05-06 02:26:19.936948 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>251</td>
        <td><a href="/get_network?sha=c4c21974a8233071db1a84996a0f9f104935a05fe57efc22e9750414f941fe41" download="weights_251.txt.gz">c4c21974</a></td>
        <td>5605.69</td>
        <td>39183</td>
        <td>15</td>
        <td>192</td>
        <td>2018-05-05 21:29:15.731843 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>250</td>
        <td><a href="/get_network?sha=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855" download="weights_250.txt.gz">e3b0c442</a></td>
        <td>5590.13</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>2018-05-05 16:44:14.691025 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>249</td>
        <td><a href="/get_network?sha=4e1a3b48fc220197f89dd121d8884f204a9ba98d979583759478b8c64461f0d5" download="weights_249.txt.gz">4e1a3b48</a></td>
        <td>5590.13</td>
        <td>29974</td>
        <td>15</td>
        <td>192</td>
        <td>2018-05-05 16:34:25.257827 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>248</td>
        <td><a href="/get_network?sha=81b4f3ac43db175ba649acdeceb0f08d7f927bf391c33d5094f0ce2377d8c35c" download="weights_248.txt.gz">81b4f3ac</a></td>
        <td>5588.32</td>
        <td>44534</td>
        <td>15</td>
        <td>192</td>
        <td>2018-05-05 11:38:52.955414 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>247</td>
        <td><a href="/get_network?sha=373d7721727c221c0cd5b7cbce3d03481ce42c8d3b2888454269704ab26ae411" download="weights_247.txt.gz">373d7721</a></td>
        <td>5582.97</td>
        <td>42937</td>
        <td>15</td>
        <td>192</td>
        <td>2018-05-05 06:45:27.661734 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>246</td>
        <td><a href="/get_network?sha=4350ce2795ebcd16c1047e024eef9caa562185abe59ef5f87b391e978eb00820" download="weights_246.txt.gz">4350ce27</a></td>
        <td>5599.02</td>
        <td>41469</td>
        <td>15</td>
        <td>192</td>
        <td>2018-05-05 01:50:48.820248 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>245</td>
        <td><a href="/get_network?sha=28a96e72040c7505b75c21a0ccae4db70ea0e85171ff978423b1bdd940521357" download="weights_245.txt.gz">28a96e72</a></td>
        <td>5595.76</td>
        <td>40380</td>
        <td>15</td>
        <td>192</td>
        <td>2018-05-04 20:52:17.319552 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>244</td>
        <td><a href="/get_network?sha=73a3e337b9ef425cadbf02255d186328774c901d505df4802ce5c6f461459cdd" download="weights_244.txt.gz">73a3e337</a></td>
        <td>5587.37</td>
        <td>42295</td>
        <td>15</td>
        <td>192</td>
        <td>2018-05-04 15:44:48.367441 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>243</td>
        <td><a href="/get_network?sha=fe73ebc527a54fc1fbaf55fdc3f0ac973b49e52656180e8f356c9867bfafb57b" download="weights_243.txt.gz">fe73ebc5</a></td>
        <td>5575.35</td>
        <td>43353</td>
        <td>15</td>
        <td>192</td>
        <td>2018-05-04 10:36:07.531725 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>242</td>
        <td><a href="/get_network?sha=ee99f620f9bb992917ea2ad4f0c0c6b3259cc92d5c81fbdecea63bc1bb84837c" download="weights_242.txt.gz">ee99f620</a></td>
        <td>5578.86</td>
        <td>55293</td>
        <td>15</td>
        <td>192</td>
        <td>2018-05-04 04:31:40.384801 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>241</td>
        <td><a href="/get_network?sha=563f1ebe92d1af43bdf890cfcb7a1fee464e7612ade61b3cdcc1254a83938fb6" download="weights_241.txt.gz">563f1ebe</a></td>
        <td>5578.41</td>
        <td>41716</td>
        <td>15</td>
        <td>192</td>
        <td>2018-05-03 23:21:42.25958 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>240</td>
        <td><a href="/get_network?sha=83d2b71a6eef92348b15f2a1ce3a27705b9582f4510dc604b6eae607e2f1c6b8" download="weights_240.txt.gz">83d2b71a</a></td>
        <td>5559.51</td>
        <td>41127</td>
        <td>15</td>
        <td>192</td>
        <td>2018-05-03 18:12:41.158076 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>239</td>
        <td><a href="/get_network?sha=0df31cb9a49e2508de58c48958c0b8726e31944ca4f533f633c2125236574d3f" download="weights_239.txt.gz">0df31cb9</a></td>
        <td>5558.62</td>
        <td>45083</td>
        <td>15</td>
        <td>192</td>
        <td>2018-05-03 13:01:13.847786 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>238</td>
        <td><a href="/get_network?sha=db0f3a5f0496213660be69974d200ea1230e63534444aaa210a8be4390563438" download="weights_238.txt.gz">db0f3a5f</a></td>
        <td>5547.21</td>
        <td>49309</td>
        <td>15</td>
        <td>192</td>
        <td>2018-05-03 07:53:15.407429 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>237</td>
        <td><a href="/get_network?sha=f49f934c6a5ef7df60aa687bdc879a5589757c810bbabe27a622a80e6c2bbfa9" download="weights_237.txt.gz">f49f934c</a></td>
        <td>5544.44</td>
        <td>47096</td>
        <td>15</td>
        <td>192</td>
        <td>2018-05-03 02:31:59.201793 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>236</td>
        <td><a href="/get_network?sha=376302cd12f9aed5a12febcd1e39ce20dfc76fc91cb1105f11895da06308563d" download="weights_236.txt.gz">376302cd</a></td>
        <td>5520.53</td>
        <td>43676</td>
        <td>15</td>
        <td>192</td>
        <td>2018-05-02 21:09:23.208958 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>235</td>
        <td><a href="/get_network?sha=18a053b5491dcf1ab790227294ed44c13ed602f536993738e60400152192bf06" download="weights_235.txt.gz">18a053b5</a></td>
        <td>5525.25</td>
        <td>43967</td>
        <td>15</td>
        <td>192</td>
        <td>2018-05-02 15:54:45.250567 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>234</td>
        <td><a href="/get_network?sha=74337e669906cb565c12a655b5b7eff4d396c5ceae01781de70c92c1d4784212" download="weights_234.txt.gz">74337e66</a></td>
        <td>5529.51</td>
        <td>44444</td>
        <td>15</td>
        <td>192</td>
        <td>2018-05-02 10:44:29.847119 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>233</td>
        <td><a href="/get_network?sha=68810cda558f541d7917c8b0351247960bcb2f7ba1ea3524990b2f6e8297f88e" download="weights_233.txt.gz">68810cda</a></td>
        <td>5512.00</td>
        <td>62833</td>
        <td>15</td>
        <td>192</td>
        <td>2018-05-02 03:37:37.261942 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>232</td>
        <td><a href="/get_network?sha=af7c437fa5947a82845935faacf9132d679efd8cd1ac22bd81cb840f65938c9f" download="weights_232.txt.gz">af7c437f</a></td>
        <td>5506.45</td>
        <td>43910</td>
        <td>15</td>
        <td>192</td>
        <td>2018-05-01 21:45:11.330886 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>231</td>
        <td><a href="/get_network?sha=85337a9e086b70795b3176ea36373d9e311a57df99600ff32ffb85e36d123f0b" download="weights_231.txt.gz">85337a9e</a></td>
        <td>5512.17</td>
        <td>55604</td>
        <td>15</td>
        <td>192</td>
        <td>2018-05-01 14:54:56.680589 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>230</td>
        <td><a href="/get_network?sha=e10f1deb8bd3a966fe9af2e8f2c2629df0639a569b4b3370487c574fb599b15e" download="weights_230.txt.gz">e10f1deb</a></td>
        <td>5506.03</td>
        <td>81484</td>
        <td>15</td>
        <td>192</td>
        <td>2018-05-01 06:05:52.364216 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>229</td>
        <td><a href="/get_network?sha=06fcbdb5074fa06226d02ed3fb42aecaf3d9d2440c78e28e4727ef38ba384c8d" download="weights_229.txt.gz">06fcbdb5</a></td>
        <td>5499.74</td>
        <td>57616</td>
        <td>15</td>
        <td>192</td>
        <td>2018-04-30 23:10:07.909408 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>228</td>
        <td><a href="/get_network?sha=40167e1af4e9ed0c679431b262e01cbc303b254d0a6481fb5e976a7cfe2c64bf" download="weights_228.txt.gz">40167e1a</a></td>
        <td>5501.10</td>
        <td>39764</td>
        <td>15</td>
        <td>192</td>
        <td>2018-04-30 18:04:25.422077 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>227</td>
        <td><a href="/get_network?sha=ed8ab720bc6485a9a9986fb9d8594102fbcfa513e6e950bbffc44f9ff8931da7" download="weights_227.txt.gz">ed8ab720</a></td>
        <td>5501.53</td>
        <td>55108</td>
        <td>15</td>
        <td>192</td>
        <td>2018-04-30 11:38:35.483537 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>226</td>
        <td><a href="/get_network?sha=e8bdc49cf2d54fc46cac1980cab6b93779814e54429c1fd93b962f9ca9e930b0" download="weights_226.txt.gz">e8bdc49c</a></td>
        <td>5403.39</td>
        <td>27595</td>
        <td>10</td>
        <td>128</td>
        <td>2018-04-30 09:30:02.571219 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>225</td>
        <td><a href="/get_network?sha=a4ebe57991afd11fb5df303bdf5a5e8212713d341f1d04a81649e97b7e7adacb" download="weights_225.txt.gz">a4ebe579</a></td>
        <td>5390.71</td>
        <td>0</td>
        <td>15</td>
        <td>192</td>
        <td>2018-04-30 07:34:35.495326 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>224</td>
        <td><a href="/get_network?sha=e7565fbf136442609fc6f5da20772e3e01a0a18cc47c3ef01eb03b914197ffa9" download="weights_224.txt.gz">e7565fbf</a></td>
        <td>5390.71</td>
        <td>43847</td>
        <td>10</td>
        <td>128</td>
        <td>2018-04-30 06:06:05.421557 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>223</td>
        <td><a href="/get_network?sha=0ac853225ae7cc5857ace8d5fdcd874d7ed492cdf30ff1352e97978f947c2dd0" download="weights_223.txt.gz">0ac85322</a></td>
        <td>5408.78</td>
        <td>42558</td>
        <td>10</td>
        <td>128</td>
        <td>2018-04-30 02:49:17.663855 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>222</td>
        <td><a href="/get_network?sha=3535f3d80e4c3ec41bb94841619b0fed7b492981bc96ecbe23d5443116c0283b" download="weights_222.txt.gz">3535f3d8</a></td>
        <td>5393.27</td>
        <td>0</td>
        <td>15</td>
        <td>192</td>
        <td>2018-04-30 01:42:25.192418 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>221</td>
        <td><a href="/get_network?sha=a75672a5ff47093396fbc50650da7e0d4fe824ef7a99c37d82bd06bc01d2fe56" download="weights_221.txt.gz">a75672a5</a></td>
        <td>5393.27</td>
        <td>38298</td>
        <td>10</td>
        <td>128</td>
        <td>2018-04-29 23:34:59.068054 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>220</td>
        <td><a href="/get_network?sha=cc2202d087f9585ab57b184d4624bc68b3dbdd88c7606699d5558ef3733227c3" download="weights_220.txt.gz">cc2202d0</a></td>
        <td>5405.26</td>
        <td>39944</td>
        <td>10</td>
        <td>128</td>
        <td>2018-04-29 20:19:41.689128 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>219</td>
        <td><a href="/get_network?sha=2eaf5ed44184446c805299d606b5f9cc8ceeb6bf1a7ff4eb0d8a2afc434f519f" download="weights_219.txt.gz">2eaf5ed4</a></td>
        <td>5402.22</td>
        <td>40759</td>
        <td>10</td>
        <td>128</td>
        <td>2018-04-29 17:03:12.762422 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>218</td>
        <td><a href="/get_network?sha=0bf50aa6bff675a26b71f63b7def210ddd70b35683877f6f7ce1ed063ce08b06" download="weights_218.txt.gz">0bf50aa6</a></td>
        <td>5396.25</td>
        <td>43539</td>
        <td>10</td>
        <td>128</td>
        <td>2018-04-29 13:48:11.288385 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>217</td>
        <td><a href="/get_network?sha=4682dc653aefb36c4fc000fd928ad511be4ce4d7139506d9758ea6be14f1271f" download="weights_217.txt.gz">4682dc65</a></td>
        <td>5405.12</td>
        <td>48021</td>
        <td>10</td>
        <td>128</td>
        <td>2018-04-29 10:28:05.501797 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>216</td>
        <td><a href="/get_network?sha=0fb0c899ede4d6e9e26dffdf3129b2b265aa9d4a1def8de9df2139e9b060b057" download="weights_216.txt.gz">0fb0c899</a></td>
        <td>5388.28</td>
        <td>52321</td>
        <td>10</td>
        <td>128</td>
        <td>2018-04-29 06:58:57.422153 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>215</td>
        <td><a href="/get_network?sha=e0bbe50a6eae41108d899d5e11453f5727ca658da0987b2f329653cba8410d0a" download="weights_215.txt.gz">e0bbe50a</a></td>
        <td>5373.22</td>
        <td>46924</td>
        <td>10</td>
        <td>128</td>
        <td>2018-04-29 03:29:17.556065 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>214</td>
        <td><a href="/get_network?sha=e26ae9b86be04d7deafe816d5c691ce88b6ef92af498fad349cff772b1c3cbe0" download="weights_214.txt.gz">e26ae9b8</a></td>
        <td>5373.22</td>
        <td>42394</td>
        <td>10</td>
        <td>128</td>
        <td>2018-04-29 00:15:17.905035 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>213</td>
        <td><a href="/get_network?sha=7bd63ace4a3384cfbd86c997c3fdea92b0bde735a8a3023e4ca786bfa8b20fe6" download="weights_213.txt.gz">7bd63ace</a></td>
        <td>5382.08</td>
        <td>39694</td>
        <td>10</td>
        <td>128</td>
        <td>2018-04-28 20:57:54.855332 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>212</td>
        <td><a href="/get_network?sha=a02f7725f06e27fc704533e6bffdb4839e7ce336c03591e73c898c8c7e3011e4" download="weights_212.txt.gz">a02f7725</a></td>
        <td>5376.90</td>
        <td>39162</td>
        <td>10</td>
        <td>128</td>
        <td>2018-04-28 17:43:12.678034 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>211</td>
        <td><a href="/get_network?sha=309dd2af3206485a4ac540d996630e8a68c62930b4563399b4be72298ddedf9f" download="weights_211.txt.gz">309dd2af</a></td>
        <td>5389.56</td>
        <td>41825</td>
        <td>10</td>
        <td>128</td>
        <td>2018-04-28 14:26:25.365184 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>210</td>
        <td><a href="/get_network?sha=f73d10407858ef11eb021438d4ec1818e44558faad31d1b398bc4d10dcf11ad5" download="weights_210.txt.gz">f73d1040</a></td>
        <td>5385.24</td>
        <td>41525</td>
        <td>10</td>
        <td>128</td>
        <td>2018-04-28 11:09:45.528785 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>209</td>
        <td><a href="/get_network?sha=d5c92bb5a378ce2f654db429c5c8676f38d4fa508a432e372742f04b85897eaa" download="weights_209.txt.gz">d5c92bb5</a></td>
        <td>5388.75</td>
        <td>4166</td>
        <td>10</td>
        <td>128</td>
        <td>2018-04-28 10:48:41.003147 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>208</td>
        <td><a href="/get_network?sha=d3cd3f9362e2c72bbc0bd63f945c3be08a4dfa312eafb92a01f54e82f170119e" download="weights_208.txt.gz">d3cd3f93</a></td>
        <td>5377.15</td>
        <td>41643</td>
        <td>10</td>
        <td>128</td>
        <td>2018-04-28 04:36:53.695667 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>207</td>
        <td><a href="/get_network?sha=341eef9fc3f22454ec09dc7476596da9b54c16990af413a5bdb746bf50727db6" download="weights_207.txt.gz">341eef9f</a></td>
        <td>5362.19</td>
        <td>41614</td>
        <td>10</td>
        <td>128</td>
        <td>2018-04-28 01:20:15.687332 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>206</td>
        <td><a href="/get_network?sha=e20848f27fae4273c5f2c4fcfef96c13593538eed8cb3e361308189100c3af2f" download="weights_206.txt.gz">e20848f2</a></td>
        <td>5372.96</td>
        <td>38851</td>
        <td>10</td>
        <td>128</td>
        <td>2018-04-27 22:04:59.366038 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>205</td>
        <td><a href="/get_network?sha=e300a2482a0d23e3f1781acd56e8071e246b1fbac913a2df070e83d1d7e664d0" download="weights_205.txt.gz">e300a248</a></td>
        <td>5358.95</td>
        <td>42431</td>
        <td>10</td>
        <td>128</td>
        <td>2018-04-27 18:48:22.050377 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>204</td>
        <td><a href="/get_network?sha=9378437f0664a907e9b020c6b734aa71dc57986a0a13ca7cbd804f42c0e336e7" download="weights_204.txt.gz">9378437f</a></td>
        <td>5361.91</td>
        <td>46699</td>
        <td>10</td>
        <td>128</td>
        <td>2018-04-27 15:30:10.430052 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>203</td>
        <td><a href="/get_network?sha=5822fe1cc68bd078fcb92b57f74603328a33b0d776167bd613f26e116da4e2d8" download="weights_203.txt.gz">5822fe1c</a></td>
        <td>5362.32</td>
        <td>45555</td>
        <td>10</td>
        <td>128</td>
        <td>2018-04-27 12:15:06.888727 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>202</td>
        <td><a href="/get_network?sha=ebe06486700e691dc6bff209545bea4f1df4b97dadc85820b4aaa0d8361597c3" download="weights_202.txt.gz">ebe06486</a></td>
        <td>5373.95</td>
        <td>44767</td>
        <td>10</td>
        <td>128</td>
        <td>2018-04-27 08:58:30.951473 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>201</td>
        <td><a href="/get_network?sha=c7316e94524e63ce44a86c32b66a319cba22cbc8b51f48643371bf7cd792bc06" download="weights_201.txt.gz">c7316e94</a></td>
        <td>5371.42</td>
        <td>47716</td>
        <td>10</td>
        <td>128</td>
        <td>2018-04-27 05:41:51.453981 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>200</td>
        <td><a href="/get_network?sha=9589169f6610c41e448b4cf699a5299d400d1cf9f6536eac71353be83f479bd7" download="weights_200.txt.gz">9589169f</a></td>
        <td>5357.75</td>
        <td>43528</td>
        <td>10</td>
        <td>128</td>
        <td>2018-04-27 02:24:18.795514 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>199</td>
        <td><a href="/get_network?sha=8c90b403e64024466230a439289733bbc21ae99f6de93b90dae5dbfcebac5df6" download="weights_199.txt.gz">8c90b403</a></td>
        <td>5364.27</td>
        <td>36632</td>
        <td>10</td>
        <td>128</td>
        <td>2018-04-26 23:00:21.026262 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>198</td>
        <td><a href="/get_network?sha=cf17a523b3e58f9995716f3d65cb7df3990d952734e72aa6a1dcba3285c20597" download="weights_198.txt.gz">cf17a523</a></td>
        <td>5356.47</td>
        <td>10867</td>
        <td>10</td>
        <td>128</td>
        <td>2018-04-26 22:04:20.666859 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>197</td>
        <td><a href="/get_network?sha=51a80158413957713103d37aa65b782fd2b344682fd51d91ccb76e71e2e63485" download="weights_197.txt.gz">51a80158</a></td>
        <td>5339.32</td>
        <td>65803</td>
        <td>10</td>
        <td>128</td>
        <td>2018-04-26 16:25:14.070828 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>196</td>
        <td><a href="/get_network?sha=8efdd3a57d2e411529bc864ab3f1bfd9df5daa8f766ec71adacd3db57f674185" download="weights_196.txt.gz">8efdd3a5</a></td>
        <td>5359.03</td>
        <td>27985</td>
        <td>10</td>
        <td>128</td>
        <td>2018-04-26 13:09:03.690848 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>195</td>
        <td><a href="/get_network?sha=55785d607471bd016e1466b3e86fb29ee76f926b9cad770e9c65599ea665c77e" download="weights_195.txt.gz">55785d60</a></td>
        <td>5341.32</td>
        <td>41793</td>
        <td>10</td>
        <td>128</td>
        <td>2018-04-26 09:51:29.939321 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>194</td>
        <td><a href="/get_network?sha=fc80cb5424adac91ed384e04020a599751d2adfa69a41afb0744de1eb375bd8f" download="weights_194.txt.gz">fc80cb54</a></td>
        <td>5345.33</td>
        <td>51843</td>
        <td>10</td>
        <td>128</td>
        <td>2018-04-26 06:27:42.580936 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>193</td>
        <td><a href="/get_network?sha=7c6b0653e734f94444543d664388d09c9c7fc7e2d861d2370611b736b4cb63ab" download="weights_193.txt.gz">7c6b0653</a></td>
        <td>5320.59</td>
        <td>44625</td>
        <td>10</td>
        <td>128</td>
        <td>2018-04-26 03:09:11.209955 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>192</td>
        <td><a href="/get_network?sha=18475f8e4155c06d0d7e5d68a2d861584d9ea29b68a6923ac7873ac9196da4ce" download="weights_192.txt.gz">18475f8e</a></td>
        <td>5322.68</td>
        <td>43860</td>
        <td>10</td>
        <td>128</td>
        <td>2018-04-25 23:52:46.695098 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>191</td>
        <td><a href="/get_network?sha=7332acd4b66124beb6bfe3ac02e95cf2922726cde889eea716f6b18326a913dc" download="weights_191.txt.gz">7332acd4</a></td>
        <td>5323.93</td>
        <td>46477</td>
        <td>10</td>
        <td>128</td>
        <td>2018-04-25 20:31:02.113078 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>190</td>
        <td><a href="/get_network?sha=3b4087e45b2f80c7f37700908ad9d795a155e38a167d7167d85f36c38e7e60ca" download="weights_190.txt.gz">3b4087e4</a></td>
        <td>5329.32</td>
        <td>45391</td>
        <td>10</td>
        <td>128</td>
        <td>2018-04-25 17:16:54.380952 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>189</td>
        <td><a href="/get_network?sha=aacdb0a3f8a3b48cbc3bae7974ef67577ca822415e5e30203f25c4aa831225ba" download="weights_189.txt.gz">aacdb0a3</a></td>
        <td>5323.33</td>
        <td>47692</td>
        <td>10</td>
        <td>128</td>
        <td>2018-04-25 13:58:43.688076 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>188</td>
        <td><a href="/get_network?sha=bb479ee94f3fb39fefb5a5b6db75bd57fd614dbd2754241730d7cb377ebb5f68" download="weights_188.txt.gz">bb479ee9</a></td>
        <td>5308.89</td>
        <td>55110</td>
        <td>10</td>
        <td>128</td>
        <td>2018-04-25 10:24:28.065843 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>187</td>
        <td><a href="/get_network?sha=088e7e0d495f91195bb9716f0f0be0b46afb7ba0f4f3158792372513d7be9ebe" download="weights_187.txt.gz">088e7e0d</a></td>
        <td>5297.69</td>
        <td>131441</td>
        <td>10</td>
        <td>128</td>
        <td>2018-04-25 02:48:39.359901 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>186</td>
        <td><a href="/get_network?sha=3ccbb451c7b83e90c05344df94bb98f5c605dba9ff20597b88158a4155a79f12" download="weights_186.txt.gz">3ccbb451</a></td>
        <td>5270.72</td>
        <td>42891</td>
        <td>10</td>
        <td>128</td>
        <td>2018-04-24 23:29:39.823909 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>185</td>
        <td><a href="/get_network?sha=14abebdda4bed5aee3186dd227bd56d33c7335609ad8446e8591e43485b60d21" download="weights_185.txt.gz">14abebdd</a></td>
        <td>5284.89</td>
        <td>48599</td>
        <td>10</td>
        <td>128</td>
        <td>2018-04-24 19:51:22.542765 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>184</td>
        <td><a href="/get_network?sha=60dbad571bda626c7ad5073077d7d17e349dbd48b123c1a4ccd1f5db46d87e47" download="weights_184.txt.gz">60dbad57</a></td>
        <td>5252.59</td>
        <td>45133</td>
        <td>10</td>
        <td>128</td>
        <td>2018-04-24 16:28:07.741811 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>183</td>
        <td><a href="/get_network?sha=486ec35cb610a0d3f8c1da44f7d8f0f4d1afe13a17431c9b1ca4abcfff5a3061" download="weights_183.txt.gz">486ec35c</a></td>
        <td>5260.00</td>
        <td>50355</td>
        <td>10</td>
        <td>128</td>
        <td>2018-04-24 13:11:26.676718 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>182</td>
        <td><a href="/get_network?sha=33f9938a2ee289edbdee41b84b7bd4201ea1560980e237ebc67bc4b827387f82" download="weights_182.txt.gz">33f9938a</a></td>
        <td>5276.70</td>
        <td>62352</td>
        <td>10</td>
        <td>128</td>
        <td>2018-04-24 09:17:23.42577 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>181</td>
        <td><a href="/get_network?sha=b3aaf42943995726e896e984d884a7d704d9f0bd5b34192dc507e47c7bd6a262" download="weights_181.txt.gz">b3aaf429</a></td>
        <td>5267.33</td>
        <td>83049</td>
        <td>10</td>
        <td>128</td>
        <td>2018-04-24 04:51:31.085911 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>180</td>
        <td><a href="/get_network?sha=fd38af17f81933dc4ddf52ad82298c8eaf370152dcb995c9de2183af03dbd3ae" download="weights_180.txt.gz">fd38af17</a></td>
        <td>5260.23</td>
        <td>55846</td>
        <td>10</td>
        <td>128</td>
        <td>2018-04-24 01:22:59.582829 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>179</td>
        <td><a href="/get_network?sha=79d7b09573d4863e27fbfa6c6807def479fba9cab466f77160392f2bdcf23dd4" download="weights_179.txt.gz">79d7b095</a></td>
        <td>5246.83</td>
        <td>47127</td>
        <td>10</td>
        <td>128</td>
        <td>2018-04-23 21:57:52.419451 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>178</td>
        <td><a href="/get_network?sha=1929922ec98046bf979017effa9e72975544935acebfc7cbe465637610745102" download="weights_178.txt.gz">1929922e</a></td>
        <td>5235.30</td>
        <td>47112</td>
        <td>10</td>
        <td>128</td>
        <td>2018-04-23 18:33:33.625038 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>177</td>
        <td><a href="/get_network?sha=1907391c74d95768aeac3ca20019da182c3a8335183b0324fbd7bedb86a9125f" download="weights_177.txt.gz">1907391c</a></td>
        <td>5220.19</td>
        <td>52129</td>
        <td>10</td>
        <td>128</td>
        <td>2018-04-23 15:07:59.370054 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>176</td>
        <td><a href="/get_network?sha=f683164bb946e23fb1824c4d900d1559f9905b04d5d6398f2a770d2f84f9b05c" download="weights_176.txt.gz">f683164b</a></td>
        <td>5213.11</td>
        <td>48295</td>
        <td>10</td>
        <td>128</td>
        <td>2018-04-23 11:46:09.567694 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>175</td>
        <td><a href="/get_network?sha=8cc0d3485503b5a880ababf06bf4b76445f94693403df09cafa728e4c8e0a2e2" download="weights_175.txt.gz">8cc0d348</a></td>
        <td>5191.50</td>
        <td>60462</td>
        <td>10</td>
        <td>128</td>
        <td>2018-04-23 08:24:46.446209 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>174</td>
        <td><a href="/get_network?sha=ebac1d4aa569128de62e55ed3f26fe3f2f4615ac79505b12bf43f6352277a1f0" download="weights_174.txt.gz">ebac1d4a</a></td>
        <td>5182.34</td>
        <td>56757</td>
        <td>10</td>
        <td>128</td>
        <td>2018-04-23 05:05:40.912423 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>173</td>
        <td><a href="/get_network?sha=101eeb41180935b487ac4c3d22610cd5b98ebb6907248e4d342a343cbb7b52bb" download="weights_173.txt.gz">101eeb41</a></td>
        <td>5176.54</td>
        <td>50526</td>
        <td>10</td>
        <td>128</td>
        <td>2018-04-23 01:43:00.201447 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>172</td>
        <td><a href="/get_network?sha=9978a784c84256c6b4021a6d29c5810b06fbfacf2557c6f6820903b21968482b" download="weights_172.txt.gz">9978a784</a></td>
        <td>5160.91</td>
        <td>44386</td>
        <td>10</td>
        <td>128</td>
        <td>2018-04-22 22:21:24.261075 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>171</td>
        <td><a href="/get_network?sha=3ecf74d5cef5325a2e50e74a2cb686121e51e7215a758596943bd2326156a932" download="weights_171.txt.gz">3ecf74d5</a></td>
        <td>5174.00</td>
        <td>44833</td>
        <td>10</td>
        <td>128</td>
        <td>2018-04-22 19:10:19.671871 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>170</td>
        <td><a href="/get_network?sha=cd9dfd24fcd4b4bde04d135796725d4c9a98fb8bb4df059de6e6b737a3c9cf05" download="weights_170.txt.gz">cd9dfd24</a></td>
        <td>5179.87</td>
        <td>63782</td>
        <td>10</td>
        <td>128</td>
        <td>2018-04-22 15:41:18.779077 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>169</td>
        <td><a href="/get_network?sha=43713a48a38a0e672f2688d4fba642a2110e70c843770bda71a35ffbac53145d" download="weights_169.txt.gz">43713a48</a></td>
        <td>5169.23</td>
        <td>68335</td>
        <td>10</td>
        <td>128</td>
        <td>2018-04-22 12:17:26.157964 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>168</td>
        <td><a href="/get_network?sha=b51830af89966cd0a6eade7f589db763cc11523f6cf21ad54b1b7173dbf79be7" download="weights_168.txt.gz">b51830af</a></td>
        <td>5160.24</td>
        <td>65389</td>
        <td>10</td>
        <td>128</td>
        <td>2018-04-22 08:59:05.402083 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>167</td>
        <td><a href="/get_network?sha=25f6d9b402c541ec8f5f3392da87604e37a1f8ae8f27976a7933e52ccd0dca31" download="weights_167.txt.gz">25f6d9b4</a></td>
        <td>5162.81</td>
        <td>62646</td>
        <td>10</td>
        <td>128</td>
        <td>2018-04-22 05:41:50.929249 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>166</td>
        <td><a href="/get_network?sha=302097818fa97d829901ecffabd8d59cfb443efc97c6c99906d3d0252e8d3ddd" download="weights_166.txt.gz">30209781</a></td>
        <td>5169.70</td>
        <td>54627</td>
        <td>10</td>
        <td>128</td>
        <td>2018-04-22 02:20:59.31669 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>165</td>
        <td><a href="/get_network?sha=c7d82781dcf8d8176da7326bc8b0bf4ee7c656ed844aeee2dfc70250b02cb8ba" download="weights_165.txt.gz">c7d82781</a></td>
        <td>5160.77</td>
        <td>55389</td>
        <td>10</td>
        <td>128</td>
        <td>2018-04-21 23:02:23.59336 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>164</td>
        <td><a href="/get_network?sha=6354b3d13eadc504e8acadf8ad74646cc138fb2317c3829a6c25a245a8c69c31" download="weights_164.txt.gz">6354b3d1</a></td>
        <td>5180.88</td>
        <td>62719</td>
        <td>10</td>
        <td>128</td>
        <td>2018-04-21 19:38:37.271187 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>163</td>
        <td><a href="/get_network?sha=890d74bade8bcdd48ba72dcb567c19ba5c158dfc2f5fd1ae83dfc58879e1b9dc" download="weights_163.txt.gz">890d74ba</a></td>
        <td>5186.43</td>
        <td>74603</td>
        <td>10</td>
        <td>128</td>
        <td>2018-04-21 15:52:39.809457 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>162</td>
        <td><a href="/get_network?sha=03b4813fe064064bd106e9a2c15ebc606503efc5ed717ba6255372206e48ddfe" download="weights_162.txt.gz">03b4813f</a></td>
        <td>5193.70</td>
        <td>63620</td>
        <td>10</td>
        <td>128</td>
        <td>2018-04-21 12:34:45.399054 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>161</td>
        <td><a href="/get_network?sha=e428a425cea359d01c670e6b08795f66fb03842f17c19bccad77f26ee88f0aa4" download="weights_161.txt.gz">e428a425</a></td>
        <td>5160.59</td>
        <td>68498</td>
        <td>10</td>
        <td>128</td>
        <td>2018-04-21 09:15:24.086358 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>160</td>
        <td><a href="/get_network?sha=a1a1e620f2b95f12132344c3e5f9ebc0bc4c4ae94fa641c40b77557bfda41bf8" download="weights_160.txt.gz">a1a1e620</a></td>
        <td>5186.78</td>
        <td>65215</td>
        <td>10</td>
        <td>128</td>
        <td>2018-04-21 05:53:48.05034 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>159</td>
        <td><a href="/get_network?sha=d2a3620413c4a42c5f3be9f7990c6a9eea3e2d871253f53275d4ec3d69d03ff4" download="weights_159.txt.gz">d2a36204</a></td>
        <td>5140.89</td>
        <td>58484</td>
        <td>10</td>
        <td>128</td>
        <td>2018-04-21 02:36:01.895101 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>158</td>
        <td><a href="/get_network?sha=02ed7b9583dc74073da20be410b7c8ccb9cc9540b4e1b80013427e3c45fe5db5" download="weights_158.txt.gz">02ed7b95</a></td>
        <td>5137.88</td>
        <td>52355</td>
        <td>10</td>
        <td>128</td>
        <td>2018-04-20 23:19:44.149433 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>157</td>
        <td><a href="/get_network?sha=d583e93ca78a917a4d5f6304bdab7b744128dc7bf51bf3acd5eb3db4d98c8c49" download="weights_157.txt.gz">d583e93c</a></td>
        <td>5134.54</td>
        <td>53666</td>
        <td>10</td>
        <td>128</td>
        <td>2018-04-20 20:02:41.586714 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>156</td>
        <td><a href="/get_network?sha=acf97b6d377167228764b6b5cfdf6a8b0e0fadcc2aec7cd717cbd84f1233f0b0" download="weights_156.txt.gz">acf97b6d</a></td>
        <td>5127.34</td>
        <td>60472</td>
        <td>10</td>
        <td>128</td>
        <td>2018-04-20 16:45:51.664363 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>155</td>
        <td><a href="/get_network?sha=cac8e6f294e4593705d45eeb0affb8233cf400e65e213f9a7ea66fcb9f158f72" download="weights_155.txt.gz">cac8e6f2</a></td>
        <td>5116.73</td>
        <td>65503</td>
        <td>10</td>
        <td>128</td>
        <td>2018-04-20 13:28:01.097302 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>154</td>
        <td><a href="/get_network?sha=61357a7cac7b1ed92f5851c73a07dde70d389dc7f4782426f8362beb5cca99b5" download="weights_154.txt.gz">61357a7c</a></td>
        <td>5120.67</td>
        <td>66171</td>
        <td>10</td>
        <td>128</td>
        <td>2018-04-20 10:09:14.482337 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>153</td>
        <td><a href="/get_network?sha=39096cabc625f8be72fd4c65ff50282ee999fa8c474c8ee1635853d46bfb74d6" download="weights_153.txt.gz">39096cab</a></td>
        <td>5071.68</td>
        <td>79614</td>
        <td>10</td>
        <td>128</td>
        <td>2018-04-20 06:09:40.602274 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>152</td>
        <td><a href="/get_network?sha=ded2a8fcf19b5bafc9742b21f72e486384880cdd402746244a6e245c2d763362" download="weights_152.txt.gz">ded2a8fc</a></td>
        <td>5073.65</td>
        <td>64484</td>
        <td>10</td>
        <td>128</td>
        <td>2018-04-20 02:52:39.185371 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>151</td>
        <td><a href="/get_network?sha=569a6fbc3461eb3f822fdf0d5f94e4cc84073cdca2e0a7b49b4739f9efe7ed0b" download="weights_151.txt.gz">569a6fbc</a></td>
        <td>5062.54</td>
        <td>72248</td>
        <td>10</td>
        <td>128</td>
        <td>2018-04-19 23:03:54.403375 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>150</td>
        <td><a href="/get_network?sha=c00b06c7c729aa6c7c0865fb5f1fb1e384c2532ba3de57b6e01b9d095454a84b" download="weights_150.txt.gz">c00b06c7</a></td>
        <td>5105.09</td>
        <td>77134</td>
        <td>10</td>
        <td>128</td>
        <td>2018-04-19 19:12:57.012734 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>149</td>
        <td><a href="/get_network?sha=55205adeaf055d09256dbe23decfec5a6f2f6a3a52f7c65b05c37936f895cabd" download="weights_149.txt.gz">55205ade</a></td>
        <td>5079.68</td>
        <td>80983</td>
        <td>10</td>
        <td>128</td>
        <td>2018-04-19 15:24:20.469018 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>148</td>
        <td><a href="/get_network?sha=602ca5be375b2f6286603a95b571ed9a3531a9a25d0b96fd08a5afea442dc042" download="weights_148.txt.gz">602ca5be</a></td>
        <td>5012.99</td>
        <td>190065</td>
        <td>10</td>
        <td>128</td>
        <td>2018-04-19 05:45:15.442803 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>147</td>
        <td><a href="/get_network?sha=5a4531c5d67cf81ded3b6f8cca3508c90dc49b5b8f225888c0318475e2d97419" download="weights_147.txt.gz">5a4531c5</a></td>
        <td>4968.40</td>
        <td>101164</td>
        <td>10</td>
        <td>128</td>
        <td>2018-04-19 00:20:54.154305 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>146</td>
        <td><a href="/get_network?sha=6c4867737c107ba608350c219dd0252ba305e349f64d90662bb02b242af78be3" download="weights_146.txt.gz">6c486773</a></td>
        <td>4944.51</td>
        <td>94720</td>
        <td>10</td>
        <td>128</td>
        <td>2018-04-18 18:57:22.511741 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>145</td>
        <td><a href="/get_network?sha=e0942492592a8060c20d35f60c7edd3ef7c1e17f775adecf46bc4de6c690a8ae" download="weights_145.txt.gz">e0942492</a></td>
        <td>4931.96</td>
        <td>115191</td>
        <td>10</td>
        <td>128</td>
        <td>2018-04-18 13:33:19.294204 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>144</td>
        <td><a href="/get_network?sha=675e8cf7a92ac1aaa8a4d9bbe3facb82b4787a6a2196d1985fb925b2baa2d08f" download="weights_144.txt.gz">675e8cf7</a></td>
        <td>4865.13</td>
        <td>105978</td>
        <td>10</td>
        <td>128</td>
        <td>2018-04-18 08:09:06.161189 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>143</td>
        <td><a href="/get_network?sha=aaf67f8e1c1a766d30e3d55eb987b4448b0d4ee421079b1beea0f3b587f42ec9" download="weights_143.txt.gz">aaf67f8e</a></td>
        <td>4893.65</td>
        <td>96765</td>
        <td>10</td>
        <td>128</td>
        <td>2018-04-18 02:43:09.364393 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>142</td>
        <td><a href="/get_network?sha=f604e3bcb343a7cad39a81791582d067c0e016c280793abe509edc4758935812" download="weights_142.txt.gz">f604e3bc</a></td>
        <td>4902.49</td>
        <td>100164</td>
        <td>10</td>
        <td>128</td>
        <td>2018-04-17 21:18:35.867993 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>141</td>
        <td><a href="/get_network?sha=5874188a811510e7b5867282296c8fc75ba4eb12b4eabcc42a3000aca7bfdc3d" download="weights_141.txt.gz">5874188a</a></td>
        <td>4897.91</td>
        <td>112039</td>
        <td>10</td>
        <td>128</td>
        <td>2018-04-17 15:56:35.098826 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>140</td>
        <td><a href="/get_network?sha=474d06260586641058ff61d6bf47f8946a3ebc6fb26a75a701ac7b1d78387e5a" download="weights_140.txt.gz">474d0626</a></td>
        <td>4867.15</td>
        <td>104827</td>
        <td>10</td>
        <td>128</td>
        <td>2018-04-17 10:31:25.06652 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>139</td>
        <td><a href="/get_network?sha=747a842bc04937b75e275581c290a19aae32bcda3dffd9c1fe767d43b97cd0cd" download="weights_139.txt.gz">747a842b</a></td>
        <td>4817.83</td>
        <td>150506</td>
        <td>10</td>
        <td>128</td>
        <td>2018-04-17 01:18:49.403481 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>138</td>
        <td><a href="/get_network?sha=536795625378faa86cac210cf66fbfddde9e01d57993e20091a7c8dec7045344" download="weights_138.txt.gz">53679562</a></td>
        <td>4828.70</td>
        <td>160845</td>
        <td>10</td>
        <td>128</td>
        <td>2018-04-16 15:51:59.267328 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>137</td>
        <td><a href="/get_network?sha=f37027dddab4379c35324eb5f10a742718f87c13ae77d9600e00dd0e25790c8a" download="weights_137.txt.gz">f37027dd</a></td>
        <td>4815.66</td>
        <td>72541</td>
        <td>10</td>
        <td>128</td>
        <td>2018-04-16 10:26:37.248066 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>136</td>
        <td><a href="/get_network?sha=31f0da5a29a5dcacc9635e5d39656b5f52c63171658cde9945bb745d3b3b7654" download="weights_136.txt.gz">31f0da5a</a></td>
        <td>4790.06</td>
        <td>69357</td>
        <td>10</td>
        <td>128</td>
        <td>2018-04-16 05:04:11.535315 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>135</td>
        <td><a href="/get_network?sha=1af5a5fb6901caffba419fe7d779c17d23e0abd5fd92a06763f3134c7b30f1be" download="weights_135.txt.gz">1af5a5fb</a></td>
        <td>4803.49</td>
        <td>64554</td>
        <td>10</td>
        <td>128</td>
        <td>2018-04-15 23:39:43.745646 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>134</td>
        <td><a href="/get_network?sha=509e13932931e0b5f854dd7fdc7340f8dd561810d6b260d5c8713938df075e66" download="weights_134.txt.gz">509e1393</a></td>
        <td>4783.36</td>
        <td>55749</td>
        <td>10</td>
        <td>128</td>
        <td>2018-04-15 18:17:44.942075 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>133</td>
        <td><a href="/get_network?sha=66916be98835ced4bb7023b94b2fae578eb2089b1b270f68e117ff7a7111bb44" download="weights_133.txt.gz">66916be9</a></td>
        <td>4805.28</td>
        <td>56037</td>
        <td>10</td>
        <td>128</td>
        <td>2018-04-15 12:55:07.743269 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>132</td>
        <td><a href="/get_network?sha=41300dcb6321189b5d291425ddd3a455fed7265bc0049f22238deb09a2340c66" download="weights_132.txt.gz">41300dcb</a></td>
        <td>4806.17</td>
        <td>44848</td>
        <td>10</td>
        <td>128</td>
        <td>2018-04-15 07:32:57.612371 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>131</td>
        <td><a href="/get_network?sha=40256ab4703cefb89f2ee7a444b5a4c44afa88c430435848441e7690cac708d2" download="weights_131.txt.gz">40256ab4</a></td>
        <td>4828.25</td>
        <td>28660</td>
        <td>10</td>
        <td>128</td>
        <td>2018-04-15 02:08:45.176534 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>130</td>
        <td><a href="/get_network?sha=0d718e4b7de65bd13f4ec6d5d3f5aeb512899fdad24f4015e743472f0912ba03" download="weights_130.txt.gz">0d718e4b</a></td>
        <td>4794.17</td>
        <td>63864</td>
        <td>10</td>
        <td>128</td>
        <td>2018-04-14 20:46:15.273269 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>129</td>
        <td><a href="/get_network?sha=c76f8661e7eb73cf50edb0f0c75d9051455d0cd0b600e30fdf0f0d25fef16de1" download="weights_129.txt.gz">c76f8661</a></td>
        <td>4871.79</td>
        <td>65310</td>
        <td>10</td>
        <td>128</td>
        <td>2018-04-14 15:22:59.950466 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>128</td>
        <td><a href="/get_network?sha=9d609b1015633361439f2fa326aadf1d1fd57514a63879fa4862035e966daf67" download="weights_128.txt.gz">9d609b10</a></td>
        <td>4766.88</td>
        <td>66540</td>
        <td>10</td>
        <td>128</td>
        <td>2018-04-14 09:58:05.189216 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>127</td>
        <td><a href="/get_network?sha=a5dd7a18edd2c2e07cac7e4c1b0b603838d96cd016fe0c3749b803274ccf16a1" download="weights_127.txt.gz">a5dd7a18</a></td>
        <td>4838.96</td>
        <td>67459</td>
        <td>10</td>
        <td>128</td>
        <td>2018-04-14 04:14:07.440142 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>126</td>
        <td><a href="/get_network?sha=d15beb5c1d0a927796f764ba383e45622fa67a51a809e6f74c2ab2685ec718aa" download="weights_126.txt.gz">d15beb5c</a></td>
        <td>4861.16</td>
        <td>60723</td>
        <td>10</td>
        <td>128</td>
        <td>2018-04-13 22:41:12.799122 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>125</td>
        <td><a href="/get_network?sha=738edc3dd6738c2aab6f625a675dad6d6fd820418af52a7731771e938fd2128b" download="weights_125.txt.gz">738edc3d</a></td>
        <td>4827.88</td>
        <td>59430</td>
        <td>10</td>
        <td>128</td>
        <td>2018-04-13 17:08:40.423322 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>124</td>
        <td><a href="/get_network?sha=5ba023b578d583d5911b299a6b99c433aa52753404493bf1aa5c4422c2f7e053" download="weights_124.txt.gz">5ba023b5</a></td>
        <td>4843.98</td>
        <td>56175</td>
        <td>10</td>
        <td>128</td>
        <td>2018-04-13 11:19:26.898456 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>123</td>
        <td><a href="/get_network?sha=f024e002e5784b010a017f1e17ced56d286019b57fe54dd3f5f13aa3c997003e" download="weights_123.txt.gz">f024e002</a></td>
        <td>4779.94</td>
        <td>159970</td>
        <td>10</td>
        <td>128</td>
        <td>2018-04-12 16:31:02.080396 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>122</td>
        <td><a href="/get_network?sha=c183f318f7b8aeaf0aa4033139784b7448fd71f07f6f95530ba6e927d5aeca70" download="weights_122.txt.gz">c183f318</a></td>
        <td>4686.33</td>
        <td>249518</td>
        <td>6</td>
        <td>64</td>
        <td>2018-04-11 09:18:36.639607 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>121</td>
        <td><a href="/get_network?sha=a6a32b9975e656cb02878b0d37dcda43735af852d48642e1fcbd95c7b9e02d50" download="weights_121.txt.gz">a6a32b99</a></td>
        <td>4694.95</td>
        <td>32575</td>
        <td>6</td>
        <td>64</td>
        <td>2018-04-11 05:00:43.225423 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>120</td>
        <td><a href="/get_network?sha=e541d28a260463401a931a30d32f0f3136d608c0ecde34bb2cf7b33c6d7c5d27" download="weights_120.txt.gz">e541d28a</a></td>
        <td>4635.64</td>
        <td>34254</td>
        <td>6</td>
        <td>64</td>
        <td>2018-04-11 00:16:33.568479 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>119</td>
        <td><a href="/get_network?sha=94c816e13232334d6b69353c23ee3185afbc3dd3ab104125131bb93aa1c26e8f" download="weights_119.txt.gz">94c816e1</a></td>
        <td>4662.68</td>
        <td>33223</td>
        <td>6</td>
        <td>64</td>
        <td>2018-04-10 19:56:54.358492 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>118</td>
        <td><a href="/get_network?sha=1d1b1a4d9d708ef04d7714b604bddea29122ec2027369e111197f7b9537b1bf8" download="weights_118.txt.gz">1d1b1a4d</a></td>
        <td>4710.17</td>
        <td>36639</td>
        <td>6</td>
        <td>64</td>
        <td>2018-04-10 15:38:09.844746 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>117</td>
        <td><a href="/get_network?sha=2340eb219ede3420debe51a02a2dc59d23263c74a887995a389cad92e1d498ae" download="weights_117.txt.gz">2340eb21</a></td>
        <td>4691.00</td>
        <td>35918</td>
        <td>6</td>
        <td>64</td>
        <td>2018-04-10 11:23:57.264572 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>116</td>
        <td><a href="/get_network?sha=3f3616dd70fafb71371edcda65c733b6fd4c9eeda7d5f8f6d0a38dfe88cac5e3" download="weights_116.txt.gz">3f3616dd</a></td>
        <td>4714.87</td>
        <td>36611</td>
        <td>6</td>
        <td>64</td>
        <td>2018-04-10 07:01:46.030343 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>115</td>
        <td><a href="/get_network?sha=fef0b4d3caec28adef4ec496692aab83c73776c8001fd050f1948077253b0160" download="weights_115.txt.gz">fef0b4d3</a></td>
        <td>4707.12</td>
        <td>35598</td>
        <td>6</td>
        <td>64</td>
        <td>2018-04-10 02:39:00.668377 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>114</td>
        <td><a href="/get_network?sha=13bfe80b80438c02f790f60b8bd1ce9b5067da4fe33dfdfc8a116547ed67d5e7" download="weights_114.txt.gz">13bfe80b</a></td>
        <td>4666.22</td>
        <td>35316</td>
        <td>6</td>
        <td>64</td>
        <td>2018-04-09 22:16:28.326851 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>113</td>
        <td><a href="/get_network?sha=2064942617b3860fd0bea6646de5e73cd7e1b24da379aefa2b408ef404568941" download="weights_113.txt.gz">20649426</a></td>
        <td>4770.97</td>
        <td>37310</td>
        <td>6</td>
        <td>64</td>
        <td>2018-04-09 17:50:10.234578 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>112</td>
        <td><a href="/get_network?sha=77b9a3a39fb8a578115c9a2b5cf7cb9c154b30197e8332fb8817fd7d0f653c16" download="weights_112.txt.gz">77b9a3a3</a></td>
        <td>4714.40</td>
        <td>38437</td>
        <td>6</td>
        <td>64</td>
        <td>2018-04-09 13:14:53.950704 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>111</td>
        <td><a href="/get_network?sha=e96cab1928eb924131b2f9d6bc7e1a7a3c457dd940b3d7cafe702a7c99bb6441" download="weights_111.txt.gz">e96cab19</a></td>
        <td>4723.58</td>
        <td>41161</td>
        <td>6</td>
        <td>64</td>
        <td>2018-04-09 08:25:17.267361 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>110</td>
        <td><a href="/get_network?sha=8e0a89b477bd34b4d690c19162b331851b1584f76c9f429ea04c7cd9a440d943" download="weights_110.txt.gz">8e0a89b4</a></td>
        <td>4717.13</td>
        <td>32442</td>
        <td>6</td>
        <td>64</td>
        <td>2018-04-09 04:07:47.783906 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>109</td>
        <td><a href="/get_network?sha=c092765386fed02f850074bd933d96bd106c69722de5afec0e7fb5d50ac9a30d" download="weights_109.txt.gz">c0927653</a></td>
        <td>4764.19</td>
        <td>34425</td>
        <td>6</td>
        <td>64</td>
        <td>2018-04-08 23:43:00.060414 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>108</td>
        <td><a href="/get_network?sha=fbff2f4dde92c9b2c817c4e54a77b4997fda9463254dd2f4f5413a4c83626533" download="weights_108.txt.gz">fbff2f4d</a></td>
        <td>4771.39</td>
        <td>34710</td>
        <td>6</td>
        <td>64</td>
        <td>2018-04-08 19:15:18.995519 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>107</td>
        <td><a href="/get_network?sha=c7479f15af92a38c2526996de5ccb39c74abc65dbb30fbee30b183446d95b084" download="weights_107.txt.gz">c7479f15</a></td>
        <td>4780.76</td>
        <td>37217</td>
        <td>6</td>
        <td>64</td>
        <td>2018-04-08 14:46:21.008138 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>106</td>
        <td><a href="/get_network?sha=b08f9afd7d64da204ed77686ef989c71ef94b26ae09233f9d92f2b6611ee5891" download="weights_106.txt.gz">b08f9afd</a></td>
        <td>4732.06</td>
        <td>37118</td>
        <td>6</td>
        <td>64</td>
        <td>2018-04-08 10:20:10.928534 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>105</td>
        <td><a href="/get_network?sha=541a5ea311b8ef740c249c27c294a2175d29ed7b97f57400cbd3329afe577fb3" download="weights_105.txt.gz">541a5ea3</a></td>
        <td>4644.06</td>
        <td>35896</td>
        <td>6</td>
        <td>64</td>
        <td>2018-04-08 06:07:25.478366 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>104</td>
        <td><a href="/get_network?sha=18b90df69aa4c40344a47609bd97d71030aa085202cb26809a81945280dbb1a1" download="weights_104.txt.gz">18b90df6</a></td>
        <td>4593.21</td>
        <td>34318</td>
        <td>6</td>
        <td>64</td>
        <td>2018-04-08 01:41:44.834979 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>103</td>
        <td><a href="/get_network?sha=3d8cec2300c3d755cb51c05108673e0058baa14e968da06d860f4892e4194bbb" download="weights_103.txt.gz">3d8cec23</a></td>
        <td>4693.56</td>
        <td>37582</td>
        <td>6</td>
        <td>64</td>
        <td>2018-04-07 20:44:44.963643 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>102</td>
        <td><a href="/get_network?sha=2e0e4c0aec16a9d10b0829eecbe854f49a30b83ab1231b8a5a520cf9ce560069" download="weights_102.txt.gz">2e0e4c0a</a></td>
        <td>4550.20</td>
        <td>66362</td>
        <td>6</td>
        <td>64</td>
        <td>2018-04-07 12:26:41.999565 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>101</td>
        <td><a href="/get_network?sha=3c0a948dd171e203abde9a61a2793162ec1c9af7f13f068b900acd16494e7f70" download="weights_101.txt.gz">3c0a948d</a></td>
        <td>4662.17</td>
        <td>33876</td>
        <td>6</td>
        <td>64</td>
        <td>2018-04-07 08:28:58.063178 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>100</td>
        <td><a href="/get_network?sha=954927f6a0a8fdb6888a6ce6280c21c7b2bb44ced2284a0afb97a5c9574ef319" download="weights_100.txt.gz">954927f6</a></td>
        <td>4567.69</td>
        <td>31840</td>
        <td>6</td>
        <td>64</td>
        <td>2018-04-07 04:32:37.999428 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>99</td>
        <td><a href="/get_network?sha=f8e58a7f84d8c7774e85e594e1a093aab17b520c79b4b7e9335553230e91b9ee" download="weights_99.txt.gz">f8e58a7f</a></td>
        <td>4635.73</td>
        <td>31353</td>
        <td>6</td>
        <td>64</td>
        <td>2018-04-07 00:36:37.609199 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>98</td>
        <td><a href="/get_network?sha=603ef658a4c8290db9fab698aec6cb246390b7d8afd4e86391ab6ca73b89e791" download="weights_98.txt.gz">603ef658</a></td>
        <td>4565.30</td>
        <td>31520</td>
        <td>6</td>
        <td>64</td>
        <td>2018-04-06 20:36:08.482644 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>97</td>
        <td><a href="/get_network?sha=d6151441286a145a3e019e00e2662656faa3c3113770bb29ea2e4cec4f872fb3" download="weights_97.txt.gz">d6151441</a></td>
        <td>4610.17</td>
        <td>0</td>
        <td>6</td>
        <td>64</td>
        <td>2018-04-06 16:37:23.177292 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>96</td>
        <td><a href="/get_network?sha=4a467e77850cbcbbf8c89145235293634fcee9f75ad15888c72f1546f97f08ae" download="weights_96.txt.gz">4a467e77</a></td>
        <td>4610.17</td>
        <td>0</td>
        <td>6</td>
        <td>64</td>
        <td>2018-04-06 12:44:32.147827 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>95</td>
        <td><a href="/get_network?sha=9c43687c48f547dda2786a77502223461e2ea1a390133d75bc730880fb0c6423" download="weights_95.txt.gz">9c43687c</a></td>
        <td>4610.17</td>
        <td>0</td>
        <td>6</td>
        <td>64</td>
        <td>2018-04-06 09:00:28.789258 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>94</td>
        <td><a href="/get_network?sha=dbe21871ecc428a9c6eedb919fba22a766851e3f7e7797e522fe1aca6e316697" download="weights_94.txt.gz">dbe21871</a></td>
        <td>4610.17</td>
        <td>256145</td>
        <td>6</td>
        <td>64</td>
        <td>2018-04-05 21:53:40.308843 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>93</td>
        <td><a href="/get_network?sha=4857f13682f53cbe936b1a2b5f6efa047bdbe917f6db4d9f6befb5bb11a6f493" download="weights_93.txt.gz">4857f136</a></td>
        <td>4608.94</td>
        <td>50699</td>
        <td>6</td>
        <td>64</td>
        <td>2018-04-05 17:54:49.256176 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>92</td>
        <td><a href="/get_network?sha=3547a8cacb7cb67c5942b6a8d9bf1e2a42f9369d19d6b3be7a7e4dff5d3183c6" download="weights_92.txt.gz">3547a8ca</a></td>
        <td>4563.67</td>
        <td>51101</td>
        <td>6</td>
        <td>64</td>
        <td>2018-04-05 14:01:50.200788 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>91</td>
        <td><a href="/get_network?sha=f808c8c4677379f38448922c8767e6e5f2965a11117ba59b0418d2214999c7bd" download="weights_91.txt.gz">f808c8c4</a></td>
        <td>4602.39</td>
        <td>45561</td>
        <td>6</td>
        <td>64</td>
        <td>2018-04-05 09:01:46.708653 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>90</td>
        <td><a href="/get_network?sha=e98e67ed6bfef7dd3b146a76b8f3a0f4d451dfd0eee07cbf0f02283f285db39c" download="weights_90.txt.gz">e98e67ed</a></td>
        <td>4579.44</td>
        <td>27896</td>
        <td>6</td>
        <td>64</td>
        <td>2018-04-05 05:05:54.270176 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>89</td>
        <td><a href="/get_network?sha=a25e364241ae6d5cf76ae2e154d7e6aacc3d1d2a3960ac0e4692c07351643349" download="weights_89.txt.gz">a25e3642</a></td>
        <td>4606.92</td>
        <td>28482</td>
        <td>6</td>
        <td>64</td>
        <td>2018-04-05 01:10:23.551457 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>88</td>
        <td><a href="/get_network?sha=b8a3961b8cd352355d58b6156792668e932c506723038a1a2568c27c8bc6514a" download="weights_88.txt.gz">b8a3961b</a></td>
        <td>4651.24</td>
        <td>49687</td>
        <td>6</td>
        <td>64</td>
        <td>2018-04-04 21:07:17.430489 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>87</td>
        <td><a href="/get_network?sha=834619c7c03ac93c08b8079559e5fc01f4ab63293b6e7f40ec02058fb0b437bd" download="weights_87.txt.gz">834619c7</a></td>
        <td>4694.18</td>
        <td>0</td>
        <td>6</td>
        <td>64</td>
        <td>2018-04-04 13:02:02.688554 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>86</td>
        <td><a href="/get_network?sha=51e2919ae1315894c371bb5f62d6ab1ad1bd93d4f64f46d8ca62ce496fb8ea77" download="weights_86.txt.gz">51e2919a</a></td>
        <td>4694.18</td>
        <td>0</td>
        <td>6</td>
        <td>64</td>
        <td>2018-04-04 09:03:01.181079 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>85</td>
        <td><a href="/get_network?sha=b15eb6f7b1b478ff6a80ec018045f97280bacbb6cda8d101e37f792fae397434" download="weights_85.txt.gz">b15eb6f7</a></td>
        <td>4694.18</td>
        <td>0</td>
        <td>6</td>
        <td>64</td>
        <td>2018-04-04 05:02:37.34845 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>84</td>
        <td><a href="/get_network?sha=7c8537e2d9f61e5ef3a996409e5815d63cdb1800e36aef4d7da8beabd658b342" download="weights_84.txt.gz">7c8537e2</a></td>
        <td>4694.18</td>
        <td>0</td>
        <td>6</td>
        <td>64</td>
        <td>2018-04-04 01:05:02.855434 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>83</td>
        <td><a href="/get_network?sha=4bcd351a6dd6113aba2764e036e88ad6d7e4143886e50d31ea5df31e9651b94a" download="weights_83.txt.gz">4bcd351a</a></td>
        <td>4694.18</td>
        <td>203346</td>
        <td>6</td>
        <td>64</td>
        <td>2018-04-03 21:06:37.75881 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>82</td>
        <td><a href="/get_network?sha=a8bdcb9dfd7b2893aeda965ff2f8b4dbc551925bf5fc4811b4a929096e7b80ad" download="weights_82.txt.gz">a8bdcb9d</a></td>
        <td>4656.61</td>
        <td>29706</td>
        <td>6</td>
        <td>64</td>
        <td>2018-04-03 17:07:51.845817 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>81</td>
        <td><a href="/get_network?sha=eaafcc53ce6038c852d3682c90c98036b4eeec11340fe4e0754f7836be9109fa" download="weights_81.txt.gz">eaafcc53</a></td>
        <td>4497.80</td>
        <td>93670</td>
        <td>6</td>
        <td>64</td>
        <td>2018-04-03 05:36:55.845498 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>80</td>
        <td><a href="/get_network?sha=52a9b7a0fdd7c34246b1ca0ea82884e88ac9f86ceee1c2539d921c108f159234" download="weights_80.txt.gz">52a9b7a0</a></td>
        <td>4505.81</td>
        <td>83959</td>
        <td>6</td>
        <td>64</td>
        <td>2018-04-02 19:27:51.061506 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>79</td>
        <td><a href="/get_network?sha=0978e7607fe0865c14e5a0d5bef1c2e5af69e2ac219ac51389d0b82ed31eb87e" download="weights_79.txt.gz">0978e760</a></td>
        <td>4478.08</td>
        <td>29280</td>
        <td>6</td>
        <td>64</td>
        <td>2018-04-02 15:38:03.857752 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>78</td>
        <td><a href="/get_network?sha=8af5b7760348d3a17504356de0d76b4a10bf7fb419049c706a6423c5de259545" download="weights_78.txt.gz">8af5b776</a></td>
        <td>4474.75</td>
        <td>43087</td>
        <td>6</td>
        <td>64</td>
        <td>2018-04-02 11:08:43.338504 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>77</td>
        <td><a href="/get_network?sha=ec518f5531b041fa7f1c7cb5db421d26e579d66ec419e7ea3f8681f6faa614ab" download="weights_77.txt.gz">ec518f55</a></td>
        <td>4419.34</td>
        <td>35043</td>
        <td>6</td>
        <td>64</td>
        <td>2018-04-02 07:27:28.002647 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>76</td>
        <td><a href="/get_network?sha=06f4a98e3e2e65a953a78a308c72c7e7b53b778fc1ceeee331b3e4b9d073cfc9" download="weights_76.txt.gz">06f4a98e</a></td>
        <td>4323.89</td>
        <td>32446</td>
        <td>6</td>
        <td>64</td>
        <td>2018-04-02 03:17:58.595475 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>75</td>
        <td><a href="/get_network?sha=a773b28388f2f183106f26bf47d531f7a3dde7e120870f19ac28373f4ff56e4b" download="weights_75.txt.gz">a773b283</a></td>
        <td>4360.11</td>
        <td>29059</td>
        <td>6</td>
        <td>64</td>
        <td>2018-04-01 23:18:06.895365 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>74</td>
        <td><a href="/get_network?sha=2908f274d49b337bd6f3a90a69d02a7de6cff9268ddfa0697cdb5345a1f7c5c8" download="weights_74.txt.gz">2908f274</a></td>
        <td>4388.26</td>
        <td>29326</td>
        <td>6</td>
        <td>64</td>
        <td>2018-04-01 19:12:30.909868 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>73</td>
        <td><a href="/get_network?sha=7f6891820fea625a7ac55410bdbc558652f3ad0e8139c249cd7cf28b8b0b6706" download="weights_73.txt.gz">7f689182</a></td>
        <td>4341.03</td>
        <td>27721</td>
        <td>6</td>
        <td>64</td>
        <td>2018-04-01 15:19:29.62667 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>72</td>
        <td><a href="/get_network?sha=2005fe39034d2ee68226126b7dbc4ae804845bac19f62198ebe854621458cb15" download="weights_72.txt.gz">2005fe39</a></td>
        <td>4368.60</td>
        <td>27803</td>
        <td>6</td>
        <td>64</td>
        <td>2018-04-01 11:11:47.626008 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>71</td>
        <td><a href="/get_network?sha=94fa288f3187a64f90eefc6cded50438ece31271ad958fa63df27a4915f501ab" download="weights_71.txt.gz">94fa288f</a></td>
        <td>4414.23</td>
        <td>0</td>
        <td>6</td>
        <td>64</td>
        <td>2018-04-01 07:17:51.02377 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>70</td>
        <td><a href="/get_network?sha=0da6631265b9f9a69fde0f05e807aeaa0a459d6785fd9cbccd8bfc5590ec1880" download="weights_70.txt.gz">0da66312</a></td>
        <td>4414.23</td>
        <td>59271</td>
        <td>6</td>
        <td>64</td>
        <td>2018-04-01 03:17:05.97253 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>69</td>
        <td><a href="/get_network?sha=0e7535a73fdbfd7b19a1f125d6c2696cee48255b8dcfff0b294b288c99b94881" download="weights_69.txt.gz">0e7535a7</a></td>
        <td>4431.85</td>
        <td>28231</td>
        <td>6</td>
        <td>64</td>
        <td>2018-03-31 23:21:44.766902 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>68</td>
        <td><a href="/get_network?sha=fb93a70743ab0b1943a1f28110f6725f6c0b384a6819232a8d71533d3a41129f" download="weights_68.txt.gz">fb93a707</a></td>
        <td>4380.64</td>
        <td>27975</td>
        <td>6</td>
        <td>64</td>
        <td>2018-03-31 19:16:04.914204 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>67</td>
        <td><a href="/get_network?sha=78e35b790c5285d291a8364136541a47972de184de0b89ecd55ff81a915fc787" download="weights_67.txt.gz">78e35b79</a></td>
        <td>4393.54</td>
        <td>28204</td>
        <td>6</td>
        <td>64</td>
        <td>2018-03-31 15:18:48.078666 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>66</td>
        <td><a href="/get_network?sha=8bb9b41bfc188a2884b4d8bcd3b87d92403f608a4b40b9cf6ea4fd3afaf0ab4d" download="weights_66.txt.gz">8bb9b41b</a></td>
        <td>4343.33</td>
        <td>0</td>
        <td>6</td>
        <td>64</td>
        <td>2018-03-31 11:15:25.2371 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>65</td>
        <td><a href="/get_network?sha=d5a36da32a7176c8c883e4e0cb8ad810c6d2d598f1e08fcfacbcbca658daf71a" download="weights_65.txt.gz">d5a36da3</a></td>
        <td>4343.33</td>
        <td>62834</td>
        <td>6</td>
        <td>64</td>
        <td>2018-03-31 07:13:08.261696 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>64</td>
        <td><a href="/get_network?sha=32fa55993d23251fd22561560f431ec46deb2e708e76367fe8df6d5bef5137b6" download="weights_64.txt.gz">32fa5599</a></td>
        <td>4279.98</td>
        <td>0</td>
        <td>6</td>
        <td>64</td>
        <td>2018-03-31 03:13:40.701628 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>63</td>
        <td><a href="/get_network?sha=0c0a29069e6f04d424d9581fe1fdc98ad833d7baf93cab8a26af3c88d315a681" download="weights_63.txt.gz">0c0a2906</a></td>
        <td>4279.98</td>
        <td>60935</td>
        <td>6</td>
        <td>64</td>
        <td>2018-03-30 23:15:20.156158 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>62</td>
        <td><a href="/get_network?sha=c065eaa17f5a1dbda74ce83889fd039cb54f4a5f70f21cb69ac1c214334155e0" download="weights_62.txt.gz">c065eaa1</a></td>
        <td>4241.64</td>
        <td>27690</td>
        <td>6</td>
        <td>64</td>
        <td>2018-03-30 19:17:07.467547 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>61</td>
        <td><a href="/get_network?sha=860fa9b753c2b560c731bc71c9d6148e9d0926fe7b0f14f52d18405486759a7e" download="weights_61.txt.gz">860fa9b7</a></td>
        <td>4224.83</td>
        <td>28238</td>
        <td>6</td>
        <td>64</td>
        <td>2018-03-30 15:13:28.488393 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>60</td>
        <td><a href="/get_network?sha=4e0ae08d57b14e8e104f7e5615650a4a1f3e8cf054eac5244aaf5b2ed57e7a03" download="weights_60.txt.gz">4e0ae08d</a></td>
        <td>4184.84</td>
        <td>0</td>
        <td>6</td>
        <td>64</td>
        <td>2018-03-30 11:15:27.759134 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>59</td>
        <td><a href="/get_network?sha=b9802872a17035c5482beb78315cf9fe021ea0688c4e9dee0c54fe5ffa8ac747" download="weights_59.txt.gz">b9802872</a></td>
        <td>4184.84</td>
        <td>55850</td>
        <td>6</td>
        <td>64</td>
        <td>2018-03-30 07:14:56.075108 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>58</td>
        <td><a href="/get_network?sha=ce9535ccf81eb66c7cea73f41848e4b3ae5963cfc348cf8efbe3d74f04aa5fa2" download="weights_58.txt.gz">ce9535cc</a></td>
        <td>4228.57</td>
        <td>0</td>
        <td>6</td>
        <td>64</td>
        <td>2018-03-30 02:36:34.524385 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>57</td>
        <td><a href="/get_network?sha=85b39b2e3efcfa0dec180ee3eb93ea257185662ddf26a8f618a598ccb3a50b52" download="weights_57.txt.gz">85b39b2e</a></td>
        <td>4228.57</td>
        <td>59535</td>
        <td>6</td>
        <td>64</td>
        <td>2018-03-29 22:38:14.304221 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>56</td>
        <td><a href="/get_network?sha=b59b6355a98c99dfa397e09005ca9a963c1c3e9bf76c9ec06f18f557bee80495" download="weights_56.txt.gz">b59b6355</a></td>
        <td>4245.95</td>
        <td>26062</td>
        <td>6</td>
        <td>64</td>
        <td>2018-03-29 18:32:26.819199 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>55</td>
        <td><a href="/get_network?sha=4b3d91552ec3bc0bca21ffe0b3383938fbf633773ca29791d44bf33e4477fec5" download="weights_55.txt.gz">4b3d9155</a></td>
        <td>4230.28</td>
        <td>52926</td>
        <td>6</td>
        <td>64</td>
        <td>2018-03-29 09:25:34.139643 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>54</td>
        <td><a href="/get_network?sha=0b93ff053467f47c57c2182e144a45c9633249519b7297c4f41fc07b30a88dd8" download="weights_54.txt.gz">0b93ff05</a></td>
        <td>4195.82</td>
        <td>0</td>
        <td>6</td>
        <td>64</td>
        <td>2018-03-29 01:51:45.82286 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>53</td>
        <td><a href="/get_network?sha=d49ef8bf753d539ee7f2cb342ce7ea8798f45595c2d6f479b938ab60e594d55c" download="weights_53.txt.gz">d49ef8bf</a></td>
        <td>4195.82</td>
        <td>0</td>
        <td>6</td>
        <td>64</td>
        <td>2018-03-29 01:10:57.183894 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>52</td>
        <td><a href="/get_network?sha=f5c40870690711889721eb0c6bc4316f19a98630f7b32daff3ec53b88610508c" download="weights_52.txt.gz">f5c40870</a></td>
        <td>4195.82</td>
        <td>0</td>
        <td>6</td>
        <td>64</td>
        <td>2018-03-28 20:43:34.979011 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>51</td>
        <td><a href="/get_network?sha=14410bc3324c9943a92d4aff8295508f6b41611932ac324b954ff8625d73bdbc" download="weights_51.txt.gz">14410bc3</a></td>
        <td>4195.82</td>
        <td>0</td>
        <td>6</td>
        <td>64</td>
        <td>2018-03-28 14:31:53.940876 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>50</td>
        <td><a href="/get_network?sha=e44821af9d4c2f78035ff313e3956a56e278c3dd4fb9a2bfbe650a9ffb3f29ff" download="weights_50.txt.gz">e44821af</a></td>
        <td>4195.82</td>
        <td>0</td>
        <td>6</td>
        <td>64</td>
        <td>2018-03-28 09:54:47.787458 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>49</td>
        <td><a href="/get_network?sha=218a136a377302cce2c645e6436b0cb8284764319046dbd5f57f7aaeb498580a" download="weights_49.txt.gz">218a136a</a></td>
        <td>4195.82</td>
        <td>122509</td>
        <td>6</td>
        <td>64</td>
        <td>2018-03-28 05:14:55.125363 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>48</td>
        <td><a href="/get_network?sha=da2308a90d124d6d2d0b8a42e3c73927b572c9bd008b623d049fe38a450e09a9" download="weights_48.txt.gz">da2308a9</a></td>
        <td>4173.35</td>
        <td>0</td>
        <td>6</td>
        <td>64</td>
        <td>2018-03-28 00:45:42.378691 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>47</td>
        <td><a href="/get_network?sha=e1bd602371901406f3c9c5a13715295f065ab0d979c3c1691316a806d6e1d4a8" download="weights_47.txt.gz">e1bd6023</a></td>
        <td>4173.35</td>
        <td>0</td>
        <td>6</td>
        <td>64</td>
        <td>2018-03-27 20:25:04.13059 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>46</td>
        <td><a href="/get_network?sha=f5baaef3db5f378f187921987bec7a31597c5040e401706a423f8d81eb830091" download="weights_46.txt.gz">f5baaef3</a></td>
        <td>4173.35</td>
        <td>0</td>
        <td>6</td>
        <td>64</td>
        <td>2018-03-27 16:12:05.882634 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>45</td>
        <td><a href="/get_network?sha=9e58022217f65691facb834379e021e5ca64ed1c1ae07594ba7f74652812e863" download="weights_45.txt.gz">9e580222</a></td>
        <td>4173.35</td>
        <td>76132</td>
        <td>6</td>
        <td>64</td>
        <td>2018-03-27 11:33:28.873373 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>44</td>
        <td><a href="/get_network?sha=c2fb7ba4a2b4ad1b81adf63201e91456532f28165a3b7f1f75ecf714aef3d48f" download="weights_44.txt.gz">c2fb7ba4</a></td>
        <td>4112.70</td>
        <td>17298</td>
        <td>6</td>
        <td>64</td>
        <td>2018-03-27 06:53:22.919137 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>43</td>
        <td><a href="/get_network?sha=8a288da9757ed4361b84f8b3f74e07a37d3309893da4e8235811538ac59e1e45" download="weights_43.txt.gz">8a288da9</a></td>
        <td>4048.49</td>
        <td>23052</td>
        <td>6</td>
        <td>64</td>
        <td>2018-03-27 00:37:05.269685 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>42</td>
        <td><a href="/get_network?sha=d9e0d1813e5d28b4c08b841ebae8b5c64e41275d81d0191961ff7708099c73e2" download="weights_42.txt.gz">d9e0d181</a></td>
        <td>3999.11</td>
        <td>16299</td>
        <td>6</td>
        <td>64</td>
        <td>2018-03-26 20:08:07.578948 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>41</td>
        <td><a href="/get_network?sha=fde903f095508a29489e629cccc2fcc49cff5ec5ac3e0ce2cec94c015aecd393" download="weights_41.txt.gz">fde903f0</a></td>
        <td>3920.26</td>
        <td>17086</td>
        <td>6</td>
        <td>64</td>
        <td>2018-03-26 15:35:14.882586 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>40</td>
        <td><a href="/get_network?sha=9692c2acff7eac6462317f56bcb3b26f5af202ae5d78bde39a1a6803d4590a81" download="weights_40.txt.gz">9692c2ac</a></td>
        <td>3885.54</td>
        <td>18334</td>
        <td>6</td>
        <td>64</td>
        <td>2018-03-26 11:08:25.181878 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>39</td>
        <td><a href="/get_network?sha=8a3a6bb4be0fd9accfc509c1a746e2a74f491c79791fadcf10b707229e9135b7" download="weights_39.txt.gz">8a3a6bb4</a></td>
        <td>3889.04</td>
        <td>0</td>
        <td>6</td>
        <td>64</td>
        <td>2018-03-26 06:38:27.016463 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>38</td>
        <td><a href="/get_network?sha=e388c9122411dc2f49a7210d75ad0650e5805966011ecc90e509402049b92dd7" download="weights_38.txt.gz">e388c912</a></td>
        <td>3889.04</td>
        <td>29812</td>
        <td>6</td>
        <td>64</td>
        <td>2018-03-26 02:07:42.222302 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>37</td>
        <td><a href="/get_network?sha=75b0a6c1b7c5a48a5d1b8ce52fc7b673adc02508a1dfc8af3ab3a10bff1ba2cb" download="weights_37.txt.gz">75b0a6c1</a></td>
        <td>3802.18</td>
        <td>15654</td>
        <td>6</td>
        <td>64</td>
        <td>2018-03-25 21:37:44.854814 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>36</td>
        <td><a href="/get_network?sha=abcee7fad011fb17cc41fb8065d29f449649c9a91f702e2d14b9da4e6305b0fe" download="weights_36.txt.gz">abcee7fa</a></td>
        <td>3740.53</td>
        <td>0</td>
        <td>6</td>
        <td>64</td>
        <td>2018-03-25 17:06:41.076864 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>35</td>
        <td><a href="/get_network?sha=a33f1e86fe2ba57db43d8bec69aa7856067eef09d1557a75c7228163027b4eb3" download="weights_35.txt.gz">a33f1e86</a></td>
        <td>3740.53</td>
        <td>0</td>
        <td>6</td>
        <td>64</td>
        <td>2018-03-25 12:37:49.192167 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>34</td>
        <td><a href="/get_network?sha=8b8b36c9212b26cf96cc62a7e7ff3ece19c115bd60a8bf1797cee291855f9484" download="weights_34.txt.gz">8b8b36c9</a></td>
        <td>3740.53</td>
        <td>0</td>
        <td>6</td>
        <td>64</td>
        <td>2018-03-25 08:05:42.940892 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>33</td>
        <td><a href="/get_network?sha=c9d2f1035a267a3f8a4f6caa717a32ed6a4f7c97358fe4098aae44a3f6716b97" download="weights_33.txt.gz">c9d2f103</a></td>
        <td>3740.53</td>
        <td>60632</td>
        <td>6</td>
        <td>64</td>
        <td>2018-03-25 03:36:59.512681 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>32</td>
        <td><a href="/get_network?sha=1034b749931253f00507bdbec9c7e81b61813545cb0f3a6f7871f5b77d345bca" download="weights_32.txt.gz">1034b749</a></td>
        <td>3693.05</td>
        <td>0</td>
        <td>6</td>
        <td>64</td>
        <td>2018-03-24 23:09:16.100157 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>31</td>
        <td><a href="/get_network?sha=dd080d5144c1f97e93dd0a36df6c676469c5aa11c6fcea78fb9d96da16b37b13" download="weights_31.txt.gz">dd080d51</a></td>
        <td>3693.05</td>
        <td>30076</td>
        <td>6</td>
        <td>64</td>
        <td>2018-03-24 18:38:45.032035 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>30</td>
        <td><a href="/get_network?sha=839e5dfb56c06ddb0cc1f817e12fe2e8ca10094ec73ed7fe2e93df945f246b63" download="weights_30.txt.gz">839e5dfb</a></td>
        <td>3670.00</td>
        <td>14558</td>
        <td>6</td>
        <td>64</td>
        <td>2018-03-24 14:07:18.955761 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>29</td>
        <td><a href="/get_network?sha=9fa03e74ea013cd77bcf8cc82c11543317a76839a912feaf6afb7aa1c7d6f1bc" download="weights_29.txt.gz">9fa03e74</a></td>
        <td>3654.16</td>
        <td>13598</td>
        <td>6</td>
        <td>64</td>
        <td>2018-03-24 09:38:02.110211 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>28</td>
        <td><a href="/get_network?sha=b630cecc83ecdc734a93de802a5fbdc2c0f29da531b05bcbd1e728d4e0c4a93a" download="weights_28.txt.gz">b630cecc</a></td>
        <td>3651.31</td>
        <td>0</td>
        <td>6</td>
        <td>64</td>
        <td>2018-03-24 05:51:42.270277 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>27</td>
        <td><a href="/get_network?sha=74287cdcfb79a9171fc5c28f2d1d12f7ac4591825dc9b95446533d731485b2a1" download="weights_27.txt.gz">74287cdc</a></td>
        <td>3651.31</td>
        <td>27824</td>
        <td>6</td>
        <td>64</td>
        <td>2018-03-24 00:56:10.576663 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>26</td>
        <td><a href="/get_network?sha=8c1c61cf495aed3fd31d1c0a86bd27132c9097b831786022d5585e94cfab7905" download="weights_26.txt.gz">8c1c61cf</a></td>
        <td>3624.36</td>
        <td>13656</td>
        <td>6</td>
        <td>64</td>
        <td>2018-03-23 20:30:25.605048 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>25</td>
        <td><a href="/get_network?sha=07cdce31df5a1a3e9cede9a84ed461e8fd0f35b9e96dd287e996142cd24920df" download="weights_25.txt.gz">07cdce31</a></td>
        <td>3576.92</td>
        <td>0</td>
        <td>6</td>
        <td>64</td>
        <td>2018-03-23 16:06:58.659328 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>24</td>
        <td><a href="/get_network?sha=f1f206203016bf5d3295c8a9fe9570609b587719da77f211822c60bd9e00e23e" download="weights_24.txt.gz">f1f20620</a></td>
        <td>3576.92</td>
        <td>0</td>
        <td>6</td>
        <td>64</td>
        <td>2018-03-23 10:39:04.989858 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>23</td>
        <td><a href="/get_network?sha=38576aeb779168c4239e53e9e8467e496c0cf6e740562743367afcacfe29f0c3" download="weights_23.txt.gz">38576aeb</a></td>
        <td>3576.92</td>
        <td>44246</td>
        <td>6</td>
        <td>64</td>
        <td>2018-03-23 06:58:51.773114 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>22</td>
        <td><a href="/get_network?sha=98240a5b3d5d27102475173ad02ed0d2cf9db033d0037183cbe4b7631366aeec" download="weights_22.txt.gz">98240a5b</a></td>
        <td>3498.75</td>
        <td>46264</td>
        <td>6</td>
        <td>64</td>
        <td>2018-03-22 16:07:56.527591 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>21</td>
        <td><a href="/get_network?sha=174b39b67c0318a0b6b831d1e96ca4e4497cd56739b5cf90d554b753afdf837b" download="weights_21.txt.gz">174b39b6</a></td>
        <td>3368.34</td>
        <td>0</td>
        <td>6</td>
        <td>64</td>
        <td>2018-03-22 07:01:01.30845 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>20</td>
        <td><a href="/get_network?sha=6a5ccda2b83e6fd8230370a6a0b3f0828e427141f1e1523f0e6b5a3ca6b7224d" download="weights_20.txt.gz">6a5ccda2</a></td>
        <td>3368.34</td>
        <td>40039</td>
        <td>6</td>
        <td>64</td>
        <td>2018-03-22 01:39:14.107847 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>19</td>
        <td><a href="/get_network?sha=209032b7bb52273db6bf66a6ad7d27616f55440a0f6c5215ad0c0a8e141fa2a7" download="weights_19.txt.gz">209032b7</a></td>
        <td>3319.15</td>
        <td>30968</td>
        <td>6</td>
        <td>64</td>
        <td>2018-03-21 14:22:58.305952 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>18</td>
        <td><a href="/get_network?sha=cd1a1e1358116ee2616239f5faaecadcdccb93e4f4102afe55a47f662c560e8c" download="weights_18.txt.gz">cd1a1e13</a></td>
        <td>3281.91</td>
        <td>22726</td>
        <td>6</td>
        <td>64</td>
        <td>2018-03-21 05:52:01.835126 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>17</td>
        <td><a href="/get_network?sha=9c9970d4bd8f6792e7d817ebccd82405c6747a0e9b4e4d1e318aa32472500590" download="weights_17.txt.gz">9c9970d4</a></td>
        <td>3135.62</td>
        <td>0</td>
        <td>6</td>
        <td>64</td>
        <td>2018-03-21 01:31:22.566016 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>16</td>
        <td><a href="/get_network?sha=6690eba0e0171644f939d36c918bd3a5f9f2e27d2ecf3e132a920a366483c905" download="weights_16.txt.gz">6690eba0</a></td>
        <td>3135.62</td>
        <td>42731</td>
        <td>6</td>
        <td>64</td>
        <td>2018-03-20 10:58:36.434199 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>15</td>
        <td><a href="/get_network?sha=f393628a290a33e1d041db6751540fd6116982604c63619024206771108e699e" download="weights_15.txt.gz">f393628a</a></td>
        <td>3033.11</td>
        <td>28047</td>
        <td>6</td>
        <td>64</td>
        <td>2018-03-19 17:37:34.125471 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>14</td>
        <td><a href="/get_network?sha=8f60220eb0eed8063ea1d5e649857592fe6566fd55a6740fcc81a231159c2068" download="weights_14.txt.gz">8f60220e</a></td>
        <td>2860.33</td>
        <td>21747</td>
        <td>6</td>
        <td>64</td>
        <td>2018-03-19 03:22:09.626405 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>13</td>
        <td><a href="/get_network?sha=5c8d14d5b1acb2f34f422e152465e005987328af7802939a131ac3f32c1f3215" download="weights_13.txt.gz">5c8d14d5</a></td>
        <td>2860.33</td>
        <td>76747</td>
        <td>6</td>
        <td>64</td>
        <td>2018-03-17 02:11:29.480216 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>12</td>
        <td><a href="/get_network?sha=1aa02cb1c436ebfab35eba03e5669dfc25ebd5e5cd312d7cad198ba3f135f38e" download="weights_12.txt.gz">1aa02cb1</a></td>
        <td>2764.14</td>
        <td>59354</td>
        <td>6</td>
        <td>64</td>
        <td>2018-03-15 11:33:03.475062 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>11</td>
        <td><a href="/get_network?sha=6d2eaec0711f67a3c04be13a7a8ee8e6e33b9719bbf889215439f024d13c68b7" download="weights_11.txt.gz">6d2eaec0</a></td>
        <td>2476.07</td>
        <td>38626</td>
        <td>6</td>
        <td>64</td>
        <td>2018-03-14 02:21:25.891241 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>10</td>
        <td><a href="/get_network?sha=7f8f398e1fda3342fdc265304635989f4fc848b1b3c7565dc0a13d839f11dd98" download="weights_10.txt.gz">7f8f398e</a></td>
        <td>2039.64</td>
        <td>12958</td>
        <td>6</td>
        <td>64</td>
        <td>2018-03-13 08:30:58.357845 -0400 EDT</td>
      </tr>
      
      <tr>
        <td>9</td>
        <td><a href="/get_network?sha=b91f353d7eda674d15573ac6c702a02e0a6ce3c8548dc0c0687f1a37fff9b7b0" download="weights_9.txt.gz">b91f353d</a></td>
        <td>1724.29</td>
        <td>60518</td>
        <td>6</td>
        <td>64</td>
        <td>2018-03-10 13:48:34.650915 -0500 EST</td>
      </tr>
      
      <tr>
        <td>8</td>
        <td><a href="/get_network?sha=03d949042474c1c9ee9c304c799a2f3478c1040c9059621812345b830499fd8e" download="weights_8.txt.gz">03d94904</a></td>
        <td>1555.89</td>
        <td>50496</td>
        <td>6</td>
        <td>64</td>
        <td>2018-03-08 16:06:44.648266 -0500 EST</td>
      </tr>
      
      <tr>
        <td>7</td>
        <td><a href="/get_network?sha=9b568ab2fe03140638848a3e9f9f76294bfd1f3f3d09641ce01cc07c61135019" download="weights_7.txt.gz">9b568ab2</a></td>
        <td>1424.95</td>
        <td>40062</td>
        <td>6</td>
        <td>64</td>
        <td>2018-03-07 01:02:15.615108 -0500 EST</td>
      </tr>
      
      <tr>
        <td>6</td>
        <td><a href="/get_network?sha=de1ddecb055da6be0468d434a5395581925277e3597a6d73718685c63cce2de3" download="weights_6.txt.gz">de1ddecb</a></td>
        <td>988.52</td>
        <td>50150</td>
        <td>6</td>
        <td>64</td>
        <td>2018-03-04 05:55:30.476115 -0500 EST</td>
      </tr>
      
      <tr>
        <td>4</td>
        <td><a href="/get_network?sha=a490ebcf43ef5f8323c3a82d08e1f7c71981a2af03bd9622e30f13a74cd589d4" download="weights_4.txt.gz">a490ebcf</a></td>
        <td>436.43</td>
        <td>38742</td>
        <td>6</td>
        <td>64</td>
        <td>2018-02-28 02:05:09.62069 -0500 EST</td>
      </tr>
      
      <tr>
        <td>3</td>
        <td><a href="/get_network?sha=45bff022a3d87c09d4f8151757fc4bd200b86115f1825c1016afcc2943cf21ef" download="weights_3.txt.gz">45bff022</a></td>
        <td>0.00</td>
        <td>9832</td>
        <td>0</td>
        <td>8</td>
        <td>2018-02-26 15:22:06.69607 -0500 EST</td>
      </tr>
      
      <tr>
        <td>2</td>
        <td><a href="/get_network?sha=e49cdc1755712f94abe6802ad44ce5101e18d43d54d73418cd8b2245cf072525" download="weights_2.txt.gz">e49cdc17</a></td>
        <td>0.00</td>
        <td>24167</td>
        <td>6</td>
        <td>64</td>
        <td>2018-02-20 00:34:39.247776 -0500 EST</td>
      </tr>
      
    </tbody>
  </table>'''

soup = BeautifulSoup(html_data, "lxml")
all_a = soup.find_all('a')
base_url = 'http://lczero.org'

for index, a in enumerate(all_a):
    if not index % 4:
        save_as = a.get('download')
        href = a.get('href')
        url = base_url + href
        subprocess.run(["wget", url, "-O", save_as])
