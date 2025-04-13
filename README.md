# HelloGame
学习游戏制作
#TODO
1.使用pyside设计界面
2.渲染库：pygame,panda3d,modernGL,pyopengl
3.物理引擎：pymunk,pybullet,box2d
4.音效：pygame,pydub等
5.输入：pyside, inputs
6.资源管理：pillow(png/jpg), pyAssimp(3d模型)，tinyobjloader(obj格式)
7.AI/行为树/路径规划:networkrx,scikit-learn
8.工具类：numpy,pyyaml/json5,loguru/watchdog

# chatgpt的建议：
my_engine/
├── core/               # 引擎核心模块（主循环、场景管理、事件调度）
│   ├── game.py
│   ├── scene.py
│   └── entity.py
├── render/             # 渲染系统（基于 Pygame 或 OpenGL）
│   └── renderer.py
├── physics/            # 物理模块（用 pymunk）
│   └── physics.py
├── input/              # 输入系统（键盘、鼠标、手柄）
│   └── input_manager.py
├── resources/          # 资源管理（图片、音频、关卡数据等）
│   └── asset_loader.py
├── editor/             # 编辑器 UI（使用 PySide6）
│   └── main_window.py
├── utils/              # 日志、热加载等工具类
│   └── logger.py
├── main.py             # 启动器
# 推荐库：
目标	库	说明
✅ UI✅ 用户界面	PySide6	Qt 设计 UI 界面和编辑器（比如场景编辑器）
✅ 渲染	Pygame	2D 渲染 + 窗口管理
✅ 物理	pymunk皮蒙克	2D 刚体/碰撞/关节等
✅ 图像加载	Pillow枕头	加载贴图、缩略图、保存等
✅ 音频	pygame.mixer	播放背景音乐和音效
✅ 输入	pygame.key / mousepygame.键/鼠标	获取输入事件
✅ 热重载✅ 热载	watchdog看门狗	资源或脚本修改时热加载（可选）
✅ 日志	loguru洛古鲁	打印调试信息，结构化日志
✅ 数据配置	PyYAML / json	游戏配置、关卡数据