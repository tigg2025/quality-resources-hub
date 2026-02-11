#!/usr/bin/env python3
"""
资源维护脚本 - 用于检查和维护资源库
"""
import json
import requests
from datetime import datetime
from typing import Dict, List

def load_resources() -> Dict:
    """加载资源数据"""
    with open('resources.json', 'r', encoding='utf-8') as f:
        return json.load(f)

def save_resources(data: Dict):
    """保存资源数据"""
    with open('resources.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def check_url(url: str) -> bool:
    """检查URL是否可访问"""
    try:
        response = requests.head(url, timeout=5, allow_redirects=True)
        return response.status_code < 400
    except:
        try:
            response = requests.get(url, timeout=5, allow_redirects=True)
            return response.status_code < 400
        except:
            return False

def check_all_resources():
    """检查所有资源的可用性"""
    data = load_resources()
    today = datetime.now().strftime('%Y-%m-%d')
    
    print(f"开始检查资源... ({today})")
    print("=" * 60)
    
    total = 0
    active = 0
    inactive = 0
    
    for category in data['categories']:
        print(f"\n{category['icon']} {category['name']}")
        print("-" * 60)
        
        for resource in category['resources']:
            total += 1
            url = resource['url']
            name = resource['name']
            
            print(f"检查: {name} ({url})...", end=' ')
            
            is_active = check_url(url)
            resource['lastChecked'] = today
            
            if is_active:
                resource['status'] = 'active'
                print("✅ 正常")
                active += 1
            else:
                resource['status'] = 'inactive'
                print("❌ 失效")
                inactive += 1
    
    # 更新最后检查时间
    data['meta']['lastUpdate'] = today
    save_resources(data)
    
    print("\n" + "=" * 60)
    print(f"检查完成！")
    print(f"总计: {total} | 正常: {active} | 失效: {inactive}")
    
    if inactive > 0:
        print(f"\n⚠️  发现 {inactive} 个失效资源，请及时处理！")

def list_resources_by_tag(tag: str):
    """按标签列出资源"""
    data = load_resources()
    results = []
    
    for category in data['categories']:
        for resource in category['resources']:
            if tag.lower() in [t.lower() for t in resource['tags']]:
                results.append({
                    'category': category['name'],
                    'name': resource['name'],
                    'url': resource['url'],
                    'description': resource['description']
                })
    
    return results

def get_active_resources() -> List[Dict]:
    """获取所有活跃的资源"""
    data = load_resources()
    results = []
    
    for category in data['categories']:
        for resource in category['resources']:
            if resource['status'] == 'active':
                results.append({
                    'category': category['name'],
                    'name': resource['name'],
                    'url': resource['url'],
                    'description': resource['description'],
                    'tags': resource['tags']
                })
    
    return results

def add_resource(category_id: str, resource: Dict):
    """添加新资源"""
    data = load_resources()
    today = datetime.now().strftime('%Y-%m-%d')
    
    # 添加默认字段
    resource['status'] = 'active'
    resource['addedDate'] = today
    resource['lastChecked'] = today
    
    # 找到对应分类并添加
    for category in data['categories']:
        if category['id'] == category_id:
            category['resources'].append(resource)
            data['meta']['lastUpdate'] = today
            save_resources(data)
            print(f"✅ 已添加资源: {resource['name']}")
            return True
    
    print(f"❌ 未找到分类: {category_id}")
    return False

if __name__ == '__main__':
    import sys
    
    if len(sys.argv) < 2:
        print("用法:")
        print("  python maintain.py check          # 检查所有资源")
        print("  python maintain.py list           # 列出所有活跃资源")
        print("  python maintain.py tag <标签>     # 按标签搜索")
        sys.exit(1)
    
    command = sys.argv[1]
    
    if command == 'check':
        check_all_resources()
    elif command == 'list':
        resources = get_active_resources()
        for r in resources:
            print(f"{r['category']} > {r['name']}: {r['url']}")
    elif command == 'tag' and len(sys.argv) > 2:
        tag = sys.argv[2]
        resources = list_resources_by_tag(tag)
        print(f"标签 '{tag}' 的资源:")
        for r in resources:
            print(f"  {r['name']}: {r['url']}")
    else:
        print("未知命令")
