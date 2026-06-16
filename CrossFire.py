#!/usr/bin/env python3
"""
🎯 CrossFire Matrix FPS - MatrixZero Engine
A first-person shooter built on mathematical matrix foundations
"""

import random
import math
import time
import sys
from typing import List, Tuple, Dict, Optional
from dataclasses import dataclass
from enum import Enum

# ============================================
# MATRIX MODULE DEFINITIONS
# ============================================

class MatrixZero:
    """Core matrix definitions for game mechanics"""
    
    # M1: Movement speed matrix (3x3)
    M1 = [
        [1/12321, 1/23432, 1/34543],
        [1/45654, 1/56765, 1/67876],
        [1/78987, 1/89098, 1/90109]
    ]
    
    # M2: Inverse precision matrix
    M2 = [
        [1/32123, 1/43234, 1/54345],
        [1/65456, 1/76567, 1/87678],
        [1/98789, 1/19891, 1/21912]
    ]
    
    # M3: Fibonacci-based damage matrix (4x4)
    M3 = [
        [1, 1, 2, 3],
        [5, 8, 13, 21],
        [34, 55, 89, 144],
        [233, 377, 600, 977]
    ]
    
    # M4: Power progression (weapon scaling)
    M4 = [
        [2, 4, 8, 16, 32],
        [64, 128, 256, 512, 1024],
        [2048, 4096, 8192, 16384],
        [32768, 65536, 131072, 262144, 524288],
        [1048576, 2097152, 4194304, 8388608, 16777216]
    ]
    
    # M5: Exponential decay matrix
    M5 = [
        [5, 25, 125, 625, 3075],
        [147949218750, 739746093750, 3698730468750, 18493652343750, 15150],
        [29589843750, 57792663574218750, 288963317871093750, 92468261718750, 75750],
        [5917968750, 11558532714843750, 2311706542968750, 462341308593750, 378750],
        [1183593750, 236718750, 47343750, 9468750, 1893750]
    ]
    
    # M6: Multiplier sequence (3x6)
    M6 = [
        [3, 6, 9, 27, 81, 243],
        [729, 2187, 6571, 19713, 59139, 177417],
        [532251, 1596753, 4790259, 14370777, 43112331, 129336993],
        [388010979, 1164032937, 34923098811, 10476296433, 31428889299, 94286667897],
        [282860003691, 848580011073, 2545740033219, 7637220099657, 22911660298971, 68734980896913]
    ]
    
    # M7: Cyclic movement pattern
    M7 = [
        [142857, 285714, 428517, 571428, 714285, 857142],
        [285714, 428517, 571428, 714285, 857142, 142857],
        [428517, 571428, 714285, 857142, 142857, 285714],
        [571428, 714285, 857142, 142857, 285714, 428517],
        [714285, 857142, 142857, 285714, 428517, 571428],
        [857142, 142857, 285714, 428517, 571428, 714285]
    ]
    
    # M8: Probability distribution matrix
    M8 = [
        [1/7, 2/7, 3/7, 4/7, 5/7, 6/7],
        [2/7, 3/7, 4/7, 5/7, 6/7, 1/7],
        [3/7, 4/7, 5/7, 6/7, 1/7, 2/7],
        [4/7, 5/7, 6/7, 1/7, 2/7, 3/7],
        [5/7, 6/7, 1/7, 2/7, 3/7, 4/7],
        [6/7, 1/7, 2/7, 3/7, 4/7, 5/7]
    ]


class Matrix345:
    """Zero-based matrices for null-state calculations"""
    
    M033 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    M044 = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    M055 = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]


class M0000:
    """Inverse open/closed string matrices"""
    M00 = [[1/102030201, 1/203040302, 1/304050403],
          [1/405060504, 1/506070605, 1/607080706],
          [1/708090807, 1/809010908, 1/901020109]]
    
    M0000 = [[1/302010203, 1/403020304, 1/504030405],
            [1/605040506, 1/706050607, 1/807060708],
            [1/908070809, 1/109080901, 1/201090102]]


class M345:
    """Fractional matrices"""
    M3 = [[1/3, 1/33, 1/333], [1/6, 1/66, 1/666], [1/9, 1/99, 1/999]]
    M4 = [[1/4, 1/44, 1/444, 1/4444], [1/8, 1/88, 1/888, 1/8888],
          [1/12, 1/1212, 1/121212, 1/12121212], [1/16, 1/1616, 1/161616, 1/16161616]]
    M5 = [[1/5, 1/55, 1/555, 1/5555, 1/55555],
          [1/10, 1/1010, 1/101010, 1/10101010, 1/1010101010],
          [1/15, 1/1515, 1/151515, 1/15151515, 1/1515151515],
          [1/20, 1/2020, 1/202020, 1/20202020, 1/2020202020],
          [1/25, 1/2525, 1/252525, 1/25252525, 1/2525252525]]


class DirectionMatrix:
    """Directional transformation matrices"""
    
    # X+ direction
    M61 = [[0, 1/7, 0, 1, 0, 0], [1/7, 0, 1/7, 0, 1, 0], [0, 1/7, 0, 0, 0, 1],
           [1, 0, 0, 0, 1/7, 0], [0, 1, 0, 1/7, 0, 1/7], [0, 0, 1, 0, 1/7, 0]]
    
    # Y+ direction
    M62 = [[0, 2/7, 0, 1, 0, 0], [2/7, 0, 2/7, 0, 1, 0], [2/7, 0, 2/7, 0, 0, 1],
           [1, 0, 0, 0, 2/7, 0], [0, 1, 0, 2/7, 0, 2/7], [0, 0, 1, 2/7, 0, 2/7]]
    
    # Z+ direction
    M63 = [[0, 3/7, 0, 1, 0, 0], [3/7, 0, 3/7, 0, 1, 0], [3/7, 0, 3/7, 0, 0, 1],
           [1, 0, 0, 0, 3/7, 0], [0, 1, 0, 3/7, 0, 3/7], [0, 0, 1, 3/7, 0, 3/7]]
    
    # Neutral positive
    M64 = [[1, 0, 1, 1, 0, 0], [1, 1, 1, 0, 1, 0], [1, 0, 1, 0, 0, 1],
           [1, 0, 0, 1, 0, 1], [0, 1, 0, 1, 1, 1], [0, 0, 1, 1, 0, 1]]
    
    # X- direction
    M66 = [[0, 0, 1, 4/7, 0, 4/7], [0, 1, 0, 0, 4/7, 0], [1, 0, 0, 4/7, 0, 4/7],
           [4/7, 0, 4/7, 0, 0, 1], [0, 4/7, 0, 0, 1, 0], [4/7, 0, 4/7, 1, 0, 0]]
    
    # Y- direction
    M67 = [[0, 0, 1, 5/7, 0, 5/7], [0, 1, 0, 0, 5/7, 0], [1, 0, 0, 0, 5/7, 0],
           [5/7, 0, 5/7, 0, 0, 1], [0, 5/7, 0, 0, 1, 0], [0, 5/7, 0, 1, 0, 0]]
    
    # Z- direction
    M68 = [[0, 0, 1, 6/7, 6/7, 6/7], [0, 1, 0, 0, 6/7, 0], [1, 0, 0, 6/7, 6/7, 6/7],
           [6/7, 6/7, 6/7, 0, 0, 1], [0, 6/7, 0, 0, 1, 0], [6/7, 6/7, 6/7, 1, 0, 0]]
    
    # Neutral negative
    M69 = [[0, 0, 1, 1, 0, 1], [0, 1, 0, 1, 1, 1], [1, 0, 0, 1, 0, 1],
           [1, 0, 1, 0, 0, 1], [1, 1, 1, 0, 1, 0], [1, 0, 1, 1, 0, 0]]


# ============================================
# GAME ENGINE
# ============================================

class WeaponType(Enum):
    PISTOL = "pistol"
    RIFLE = "rifle"
    SHOTGUN = "shotgun"
    SNIPER = "sniper"
    GRENADE = "grenade"

@dataclass
class Weapon:
    """Weapon definition using matrix-derived stats"""
    name: str
    weapon_type: WeaponType
    damage: int
    fire_rate: float
    accuracy: float
    range: int
    ammo: int
    max_ammo: int
    
    @classmethod
    def create_from_matrix(cls, weapon_type: WeaponType, tier: int):
        """Create weapon using M4 power progression and M3 damage"""
        mz = MatrixZero()
        base_damage = mz.M3[tier % 4][tier % 4]
        fire_rate_mult = mz.M4[tier % 5][0] / 100
        
        weapons = {
            WeaponType.PISTOL: cls("Pistol", WeaponType.PISTOL, 
                                   int(base_damage * 10), 0.5 * fire_rate_mult, 
                                   0.7, 50, 12, 12),
            WeaponType.RIFLE: cls("Rifle", WeaponType.RIFLE,
                                  int(base_damage * 25), 0.1 * fire_rate_mult,
                                  0.85, 200, 30, 30),
            WeaponType.SHOTGUN: cls("Shotgun", WeaponType.SHOTGUN,
                                    int(base_damage * 40), 0.8 * fire_rate_mult,
                                    0.5, 30, 8, 8),
            WeaponType.SNIPER: cls("Sniper", WeaponType.SNIPER,
                                   int(base_damage * 80), 1.5 * fire_rate_mult,
                                   0.95, 500, 5, 5),
            WeaponType.GRENADE: cls("Grenade", WeaponType.GRENADE,
                                    int(base_damage * 60), 2.0 * fire_rate_mult,
                                    0.6, 40, 3, 3)
        }
        return weapons[weapon_type]


@dataclass
class Player:
    """Player with matrix-based attributes"""
    name: str
    health: float = 100.0
    armor: float = 50.0
    position: List[float] = None
    velocity: List[float] = None
    weapon: Weapon = None
    kills: int = 0
    deaths: int = 0
    
    def __post_init__(self):
        if self.position is None:
            self.position = [0.0, 0.0, 0.0]
        if self.velocity is None:
            self.velocity = [0.0, 0.0, 0.0]
    
    def move(self, direction: List[int], delta_time: float):
        """Move player using M7 cyclic patterns"""
        mz = MatrixZero()
        pattern_row = mz.M7[abs(int(self.position[0])) % 6]
        speed = pattern_row[abs(int(self.position[1])) % 6] / 100000
        
        self.position[0] += direction[0] * speed * delta_time
        self.position[1] += direction[1] * speed * delta_time
        self.position[2] += direction[2] * speed * delta_time
    
    def take_damage(self, damage: float):
        """Apply damage using M8 probability distribution"""
        mz = MatrixZero()
        prob = mz.M8[random.randint(0, 5)][random.randint(0, 5)]
        
        if self.armor > 0:
            armor_absorb = damage * 0.5
            self.armor = max(0, self.armor - armor_absorb)
            damage *= 0.5
        
        if random.random() < prob:
            damage *= 1.5  # Critical hit
            print("💥 CRITICAL HIT!")
        
        self.health = max(0, self.health - damage)


class Map:
    """Game map generated from matrices"""
    
    def __init__(self, size: int = 100):
        self.size = size
        self.grid = self._generate_terrain()
        self.spawn_points = self._generate_spawns()
        self.power_ups = []
        self.obstacles = self._generate_obstacles()
    
    def _generate_terrain(self) -> List[List[int]]:
        """Generate terrain using M9 matrix patterns"""
        mz = MatrixZero()
        terrain = []
        for i in range(min(9, self.size)):
            row = []
            for j in range(min(9, self.size)):
                # Use M9-like pattern
                value = (i * j + i + j) % 3
                row.append(value)
            terrain.append(row)
        return terrain
    
    def _generate_spawns(self) -> List[List[float]]:
        """Generate spawn points using M7 pattern"""
        mz = MatrixZero()
        spawns = []
        for i in range(4):
            spawn = [
                mz.M7[i][0] / 10000,
                0,
                mz.M7[i][2] / 10000
            ]
            spawns.append(spawn)
        return spawns
    
    def _generate_obstacles(self) -> List[Dict]:
        """Generate obstacles using matrix patterns"""
        obstacles = []
        mz = MatrixZero()
        for i in range(10):
            obstacle = {
                'position': [
                    random.uniform(-self.size, self.size),
                    random.uniform(0, 5),
                    random.uniform(-self.size, self.size)
                ],
                'size': mz.M1[i % 3][i % 3] / 10000,
                'type': random.choice(['wall', 'crate', 'barrel'])
            }
            obstacles.append(obstacle)
        return obstacles


class CrossFireGame:
    """Main CrossFire FPS Game"""
    
    def __init__(self):
        self.players: List[Player] = []
        self.map = Map()
        self.score_team_a = 0
        self.score_team_b = 0
        self.round_time = 180  # 3 minutes
        self.current_time = 0
        self.game_mode = "Team Deathmatch"
        self.running = False
        
        # Matrix instances
        self.mz = MatrixZero()
        self.dir_matrix = DirectionMatrix()
    
    def create_player(self, name: str, team: str) -> Player:
        """Create player with matrix-derived starting stats"""
        spawn_idx = len(self.players) % 4
        spawn = self.map.spawn_points[spawn_idx].copy()
        
        if team == "B":
            spawn[0] *= -1
            spawn[2] *= -1
        
        player = Player(name=name, position=spawn)
        
        # Give starting weapon based on team
        if team == "A":
            player.weapon = Weapon.create_from_matrix(WeaponType.RIFLE, 0)
        else:
            player.weapon = Weapon.create_from_matrix(WeaponType.RIFLE, 2)
        
        self.players.append(player)
        return player
    
    def calculate_damage(self, attacker: Player, target: Player, distance: float) -> float:
        """Calculate damage using M3 Fibonacci matrix"""
        m3 = self.mz.M3
        base_damage = attacker.weapon.damage
        
        # Distance falloff using M3 pattern
        distance_factor = 1.0
        if distance > attacker.weapon.range:
            distance_factor = m3[min(int(distance/10), 3)][min(int(distance/10), 3)] / 100
        
        # Accuracy using M8 probability
        accuracy_roll = random.random()
        if accuracy_roll > attacker.weapon.accuracy:
            return 0  # Miss
        
        return base_damage * distance_factor
    
    def shoot(self, shooter: Player, target_pos: List[float]):
        """Handle shooting mechanics with matrix-based calculations"""
        if shooter.weapon.ammo <= 0:
            print("🔫 Click... Out of ammo!")
            return
        
        shooter.weapon.ammo -= 1
        
        # Calculate distance to target
        dx = target_pos[0] - shooter.position[0]
        dy = target_pos[1] - shooter.position[1]
        dz = target_pos[2] - shooter.position[2]
        distance = math.sqrt(dx*dx + dy*dy + dz*dz)
        
        # Check all players for hits
        for target in self.players:
            if target == shooter:
                continue
            
            # Calculate actual distance to player
            tdx = target.position[0] - shooter.position[0]
            tdy = target.position[1] - shooter.position[1]
            tdz = target.position[2] - shooter.position[2]
            target_distance = math.sqrt(tdx*tdx + tdy*tdy + tdz*tdz)
            
            # Hit detection using weapon range
            if target_distance <= shooter.weapon.range:
                # Calculate angle using direction matrix
                angle = math.atan2(tdz, tdx)
                hit_chance = shooter.weapon.accuracy
                
                # Use M8 matrix for hit probability
                m8_row = int(abs(angle * 3)) % 6
                m8_col = int(target_distance / 10) % 6
                if m8_row < 6 and m8_col < 6:
                    hit_chance *= self.mz.M8[m8_row][m8_col]
                
                if random.random() < hit_chance:
                    damage = self.calculate_damage(shooter, target, target_distance)
                    if damage > 0:
                        target.take_damage(damage)
                        print(f"🎯 {shooter.name} hit {target.name} for {damage:.1f} damage!")
                        
                        if target.health <= 0:
                            self.handle_kill(shooter, target)
    
    def handle_kill(self, killer: Player, victim: Player):
        """Handle kill events"""
        killer.kills += 1
        victim.deaths += 1
        
        # Award points using M6 multiplier
        points = int(self.mz.M6[0][min(killer.kills % 6, 5)] / 100)
        print(f"☠️  {killer.name} eliminated {victim.name}! (+{points} points)")
        
        # Respawn victim
        spawn_idx = victim.deaths % 4
        victim.position = self.map.spawn_points[spawn_idx].copy()
        victim.health = 100
        victim.armor = 50
        victim.weapon.ammo = victim.weapon.max_ammo
    
    def apply_power_up(self, player: Player):
        """Apply power-up using M5 exponential matrix"""
        power_ups = ["health", "armor", "damage", "speed", "ammo"]
        pu_type = random.choice(power_ups)
        
        # Use M5 for power-up magnitude
        m5 = self.mz.M5
        magnitude = m5[random.randint(0, 4)][0] / 1000000
        
        if pu_type == "health":
            player.health = min(100, player.health + 25 * magnitude)
            print(f"💚 Health restored!")
        elif pu_type == "armor":
            player.armor = min(100, player.armor + 30 * magnitude)
            print(f"🛡️  Armor boosted!")
        elif pu_type == "ammo":
            player.weapon.ammo = player.weapon.max_ammo
            print(f"🔋 Ammo refilled!")
    
    def display_game_state(self):
        """Display current game state"""
        print("\n" + "="*60)
        print(f"🎮 CROSSFIRE MATRIX FPS | {self.game_mode}")
        print("="*60)
        print(f"⏱️  Time: {self.current_time:.0f}s / {self.round_time}s")
        print(f"📊 Score - Team A: {self.score_team_a} | Team B: {self.score_team_b}")
        print("-"*60)
        
        for i, player in enumerate(self.players):
            team = "A" if i % 2 == 0 else "B"
            health_bar = "█" * int(player.health/10) + "░" * (10 - int(player.health/10))
            print(f"[{team}] {player.name}")
            print(f"    ❤️  {health_bar} {player.health:.0f}%")
            print(f"    🛡️  Armor: {player.armor:.0f} | 🔫 {player.weapon.name}")
            print(f"    🎯 K/D: {player.kills}/{player.deaths} | 💊 Ammo: {player.weapon.ammo}")
            print(f"    📍 Pos: ({player.position[0]:.1f}, {player.position[1]:.1f}, {player.position[2]:.1f})")
        
        print("="*60)
    
    def menu(self):
        """Game menu"""
        print("""
╔══════════════════════════════════════════╗
║     🎯 CROSSFIRE MATRIX FPS 🎯          ║
║         MatrixZero Engine v1.0           ║
╚══════════════════════════════════════════╝

[1] 🎮 Start Match
[2] 👤 Add Player (Bot)
[3] 🔫 Change Weapon
[4] 🗺️  View Map Info
[5] 📊 View Matrices
[6] ℹ️  Help
[0] 🚪 Exit
""")
    
    def run(self):
        """Main game loop"""
        self.running = True
        
        # Create default players
        self.create_player("Alpha", "A")
        self.create_player("Bravo", "B")
        
        while self.running:
            self.menu()
            choice = input("\n🎯 Select action: ").strip()
            
            if choice == "1":
                self.start_match()
            elif choice == "2":
                name = input("Enter bot name: ")
                team = input("Team (A/B): ").upper()
                if team in ["A", "B"]:
                    self.create_player(name, team)
                    print(f"✅ {name} joined Team {team}!")
            elif choice == "3":
                self.change_weapon_menu()
            elif choice == "4":
                self.show_map_info()
            elif choice == "5":
                self.show_matrices()
            elif choice == "6":
                self.show_help()
            elif choice == "0":
                print("👋 Exiting CrossFire Matrix FPS...")
                self.running = False
            else:
                print("❌ Invalid choice!")
    
    def start_match(self):
        """Start a match simulation"""
        if len(self.players) < 2:
            print("❌ Need at least 2 players!")
            return
        
        print(f"\n🔥 MATCH START! {self.game_mode}")
        print(f"Players: {len(self.players)} | Map Size: {self.map.size}x{self.map.size}")
        time.sleep(1)
        
        # Simulate match
        self.current_time = 0
        match_duration = 30  # Short simulation
        
        while self.current_time < match_duration and self.running:
            self.current_time += 1
            
            # Random player actions
            for player in self.players:
                # Random movement using direction matrices
                direction = [
                    random.choice([-1, 0, 1]),
                    random.choice([-1, 0, 1]),
                    random.choice([-1, 0, 1])
                ]
                player.move(direction, 1.0)
                
                # Random shooting
                if random.random() < 0.3:  # 30% chance to shoot
                    target = random.choice(self.players)
                    if target != player:
                        self.shoot(player, target.position)
                
                # Random power-up spawn
                if random.random() < 0.1:  # 10% chance
                    self.apply_power_up(player)
            
            # Display state every 5 seconds
            if self.current_time % 5 == 0:
                self.display_game_state()
                time.sleep(0.5)
        
        print("\n🏁 MATCH ENDED!")
        self.display_game_state()
    
    def change_weapon_menu(self):
        """Change player weapon"""
        print("\n🔫 Weapon Selection:")
        print("[1] Pistol")
        print("[2] Rifle")
        print("[3] Shotgun")
        print("[4] Sniper")
        print("[5] Grenade")
        
        choice = input("Select weapon: ")
        weapon_map = {
            "1": WeaponType.PISTOL,
            "2": WeaponType.RIFLE,
            "3": WeaponType.SHOTGUN,
            "4": WeaponType.SNIPER,
            "5": WeaponType.GRENADE
        }
        
        if choice in weapon_map and self.players:
            player = self.players[0]  # First player
            player.weapon = Weapon.create_from_matrix(weapon_map[choice], player.kills)
            print(f"✅ {player.name} equipped {player.weapon.name}!")
    
    def show_map_info(self):
        """Display map information"""
        print(f"\n🗺️  Map Information:")
        print(f"Size: {self.map.size}x{self.map.size}")
        print(f"Obstacles: {len(self.map.obstacles)}")
        print(f"Spawn Points: {len(self.map.spawn_points)}")
        
        # Show terrain using M1 matrix
        print("\nTerrain Matrix (M1):")
        for row in self.mz.M1:
            print("  ", row)
    
    def show_matrices(self):
        """Display all matrix modules"""
        print("\n📊 Matrix Modules:")
        print("M1 - Movement Speed:")
        for row in self.mz.M1:
            print(f"  {row}")
        print("\nM3 - Damage Fibonacci:")
        for row in self.mz.M3:
            print(f"  {row}")
        print("\nM4 - Power Progression:")
        for row in self.mz.M4[:3]:
            print(f"  {row}")
        print("  ...")
    
    def show_help(self):
        """Show help information"""
        print("""
🎮 CROSSFIRE MATRIX FPS - HELP
════════════════════════════════════
This game uses mathematical matrices for all mechanics:

M1: Movement speed calculation
M2: Inverse precision for weapon spread
M3: Fibonacci damage scaling
M4: Power progression for weapons
M5: Exponential decay for power-ups
M6: Score multipliers
M7: Cyclic movement patterns
M8: Probability distribution for hits
M9: General game patterns

Controls:
- Add bots and watch them fight
- Matrices determine everything!
- Each matrix affects different game aspects
""")


# ============================================
# MAIN ENTRY POINT
# ============================================

def main():
    """Main entry point"""
    print("""
╔══════════════════════════════════════════╗
║     🎯 CROSSFIRE MATRIX FPS 🎯          ║
║         MatrixZero Engine v1.0           ║
║     Powered by Mathematical Matrices     ║
╚══════════════════════════════════════════╝
    
Loading Matrix Modules...
    """)
    
    # Verify matrix loading
    mz = MatrixZero()
    print(f"✅ M1 Movement Matrix: {len(mz.M1)}x{len(mz.M1[0])}")
    print(f"✅ M3 Damage Matrix: {len(mz.M3)}x{len(mz.M3[0])}")
    print(f"✅ M4 Power Matrix: {len(mz.M4)}x{len(mz.M4[0])}")
    print(f"✅ M7 Cyclic Matrix: {len(mz.M7)}x{len(mz.M7[0])}")
    print(f"✅ M8 Probability Matrix: {len(mz.M8)}x{len(mz.M8[0])}")
    print(f"✅ Direction Matrices Loaded")
    print("\n🎮 MatrixZero Engine Ready!\n")
    
    try:
        game = CrossFireGame()
        game.run()
    except KeyboardInterrupt:
        print("\n\n👋 Game interrupted. Exiting...")
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()