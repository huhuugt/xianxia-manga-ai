#!/usr/bin/env python3
"""
100岁老人修仙 - 特定题材生成脚本
生成关于百岁老人逆天修仙的完整漫剧
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import json
from src.hermes_agent import HermesAgent
from src.manga_generator import MangaGenerator
from src.utils import setup_logging, ColoredOutput, print_section

def generate_elderly_cultivation_manga():
    """生成100岁老人修仙漫剧"""
    
    # 设置日志
    setup_logging(log_level="INFO", log_file="output/elderly_cultivation.log")
    
    print_section("🧓 100岁老人修仙漫剧生成系统", 70)
    
    # 初始化
    agent = HermesAgent()
    generator = MangaGenerator(agent)
    
    # 定制配置
    config = {
        "title": "百岁仙途",
        "theme": "老年逆袭",
        "episodes": 5,
        "style": "温情冒险",
        "protagonist": """
        一位100岁的普通老人，本已步入人生暮年，却因机缘巧合觉醒了灵根。
        虽然年迈，但他决定踏上修仙之路，用余生去追求永恒的生命和力量。
        他用智慧和经验弥补体质的不足，证明修仙之路没有年龄限制。
        """,
        "world_setting": "当代都市+秘密修仙世界",
        "save_output": True
    }
    
    print("\n📜 漫剧设定信息：")
    print(f"  标题：{config['title']}")
    print(f"  主题：{config['theme']}")
    print(f"  风格：{config['style']}")
    print(f"  话数：{config['episodes']}")
    print(f"  背景：{config['world_setting']}")
    print(f"  主角：{config['protagonist'].strip()}")
    
    # 生成漫剧
    print("\n⏳ 正在生成漫剧，请稍候...\n")
    
    result = generator.generate_with_config(config)
    
    if "error" in result:
        ColoredOutput.print_error(f"生成失败：{result['error']}")
        return
    
    ColoredOutput.print_success("✨ 漫剧生成完成！")
    
    # 打印结果摘要
    summary = generator.get_summary()
    
    print_section("📖 漫剧信息", 70)
    print(f"标题：{summary['title']}")
    print(f"主题：{summary['theme']}")
    print(f"风格：{summary['style']}")
    print(f"话数：{summary['episodes_count']}")
    print(f"生成时间：{summary['generated_at']}")
    
    print("\n📺 故事大纲：")
    for ep in summary['episodes']:
        print(f"\n  第{ep['no']}话：{ep['title']}")
        print(f"  梗概：{ep['summary'][:100]}...")
    
    # 保存完整数据
    output_file = f"output/百岁仙途_{summary['episodes_count']}话_完整版.json"
    generator.export(output_file, format="json")
    ColoredOutput.print_success(f"✓ 完整数据已保存到：{output_file}")
    
    # 保存 Markdown 版本
    md_file = f"output/百岁仙途_{summary['episodes_count']}话_完整版.md"
    generator.export(md_file, format="markdown")
    ColoredOutput.print_success(f"✓ Markdown 版本已保存到：{md_file}")
    
    # 显示第一话的详细内容
    if result.get('episodes'):
        print_section("📚 第一话详细内容（示例）", 70)
        first_episode = result['episodes'][0]
        print(f"话标题：{first_episode['title']}")
        print(f"梗概：{first_episode['summary']}")
        
        content = first_episode.get('content', {})
        if isinstance(content, dict):
            print("\n场景内容：")
            for key, value in list(content.items())[:2]:  # 显示前两个场景
                print(f"\n【{key}】")
                print(str(value)[:300] + "...\n")
    
    return result


def interactive_elderly_cultivation():
    """交互式100岁老人修仙创意讨论"""
    
    setup_logging(log_level="INFO")
    
    print_section("💬 与 Hermes Agent 讨论100岁老人修仙创意", 70)
    
    agent = HermesAgent()
    
    # 测试连接
    print("正在连接 Agent...\n")
    if not agent.test_agent():
        ColoredOutput.print_error("Agent 连接失败")
        return
    
    ColoredOutput.print_success("Agent 连接成功！\n")
    
    # 预设对话
    discussions = [
        "设计一位100岁老人修仙的设定。他应该有什么特点和经历？",
        "作为100岁的老人，他修仙的优势和劣势分别是什么？",
        "请为这位老人设计一个有趣的修仙机遇或转折点。",
        "这部作品的主要冲突和故事线应该是什么？"
    ]
    
    for i, question in enumerate(discussions, 1):
        print(f"【问题 {i}】{question}\n")
        
        response = agent.chat(question)
        if response:
            print(f"【Agent 回答】\n{response[:500]}...\n")
            print("-" * 70 + "\n")
        
        if i < len(discussions):
            input("按 Enter 继续下一个问题...")
    
    # 保存对话
    agent.export_conversation("output/elderly_cultivation_discussion.json")
    ColoredOutput.print_success("对话已保存")


def main():
    """主程序"""
    
    print("""
╔════════════════════════════════════════════════════════════════════╗
║                                                                    ║
║            🧓 100岁老人修仙漫剧 - AI 生成系统                     ║
║                                                                    ║
║   用 Hermes Agent + DeepSeek V4 创作老年逆袭的奇幻故事           ║
║                                                                    ║
╚════════════════════════════════���═══════════════════════════════════╝
    """)
    
    print("请选择操作：")
    print("1. 生成完整漫剧")
    print("2. 与 Agent 讨论创意")
    print("0. 退出")
    
    choice = input("\n请输入选择 (0-2): ").strip()
    
    if choice == "1":
        generate_elderly_cultivation_manga()
    elif choice == "2":
        interactive_elderly_cultivation()
    elif choice == "0":
        print("再见！")
        return
    else:
        print("无效选择")
    
    print("\n✨ 操作完成！")
    print("📁 所有输出文件已保存到 output/ 目录")


if __name__ == "__main__":
    main()
