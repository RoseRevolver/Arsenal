@echo off
title 每天毒一点
color 0a
:menu
cls
echo==========================
echo 欢迎品尝今天的毒鸡汤
echo==========================
echo.
echo==========================
echo 1.接受毒鸡汤
echo 2.拒绝毒鸡汤
echo 3.退出
echo==========================
set /p num=请输入数字
if "%num%" == "1" goto 1
if "%num%" == "2" goto 2
if "%num%" == "3" goto 3
 
echo 就tm你行？就tm你明白？别tm乱输入，按规矩来！
pause >nul 2>nul
goto menu
:1
echo   打工人打工魂打工都是人上人！！！！！
echo   加油！今天工地的砖头依然烫手！
echo   碧赛！碧赛！发硬的红！背背背背起了行囊。
pause >nul 2>nul
goto menu
:2
echo 你怎么能够妥协呢？不能拒绝，必须给我干了这碗毒鸡汤！
echo   打工人打工魂打工都是人上人！！！！！
echo   加油！今天工地的砖头依然烫手！
echo   碧赛！碧赛！发硬的红！背背背背起了行囊。
pause >nul 2>nul
goto menu
:3
exit
