1. 學號：           R05522625
2. 姓名：           王威翔
3. 使用之程式語言： C++ (c++17)
4. 使用之編譯器：   GNU g++ 
5. 檔案壓縮方式:    zip
6. 各檔案說明：
    main.cpp:          主程式
    main_noGraph.cpp:  主程式(無作圖功能版本)
    makefile:          自動化建構指令
    build:             執行檔
    out:               執行範例輸入檔test.in之輸出檔
    out_5x5:           執行範例輸入檔test_5x5.in之輸出檔
    out_7x7:           執行範例輸入檔test_7x7.in之輸出檔
    test.in.jpg:       執行範例輸入檔test.in之輸出作圖
    test_5x5.in.jpg:   執行範例輸入檔test_5x5.in之輸出作圖
    test_7x7.in.jpg:   執行範例輸入檔test_7x7.in之輸出作圖

7. 編譯方式說明：
   主程式：main.cpp
     請在主程式的目錄下，鍵入make指令，即可完成編譯
     ( Makefile指定之 Optimize 指令為 -O3 )，
     若電腦無法正常使用GNU plot，則改用make noGraph指令，
     編譯不會作圖之執行檔

8. 執行、使用方式說明：
   主程式：
    編譯完成後，在檔案目錄下會產生一個 build 的執行檔
    執行檔的命令格式為：

        ./built <input file name> <output file name>

    例如：要以 test.in 內的資訊作Bezier Curve並將取樣點座標輸出於
    test.out並作圖，則在命令提示下鍵入：

        ./build test.in test.out

    便會在目錄下自動生成(1)含取樣點座標的檔案test.out 和
                        (2)與輸入檔同名之jpg檔 (若以make noGrpah編譯則無)

9. 執行結果說明：
   主程式：
     主程式執行結束後會在 console 輸出總執行時間，如：
     
         Time taken: 6.86s

   輸出檔：
     每行包含取樣點的x, y座標，以製表符("\t")隔開

   作圖：
     包含以紅色繪製的Control Point連線及藍色繪製的Bezier Curve

10. 共同討論者與參考資料：
   a. 此份程式在與 課堂助教呂祐昇 及 修課同學李尚軒 討論後完成
   
   b. Bezier Curves -- Denis Rizov
      https://denisrizov.com/2016/06/02/bezier-curves-unity-package-included/

   c. GNUplot標頭檔(來自Google Code Archive)
      https://code.google.com/archive/p/gnuplot-cpp/downloads

   d. Demos for gnuplot version 5.2
      http://gnuplot.sourceforge.net/demo_5.2/
