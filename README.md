# Robotics Math Basics

This mini-project is part of my daily **robotics and autonomous systems learning practice**.

It implements the core 2D math utilities used everywhere in robotics:
- Degrees ↔ radians conversion
- 2D rotation matrices
- Rotating a point in space
- Translation (shifting a point)
- Combining rotation + translation → 2D transform
- Composing two transforms (frame chaining)

The demos are shown in `main.py`.

---

## 📂 Project Structure

robotics-math-basics/  
│  
├── robotics_math.py   — Core robotics math utilities  
├── main.py            — Demo / usage examples  
└── README.md

---

## 🚀 How to Run

Requirements: **Python 3.x**

Run the demo:

```bash
python main.py
```

---

## 🔥 Key Concepts Learned

### 1️⃣ Degrees vs Radians
Humans use **degrees**.  
Robots and mathematics use **radians** because trigonometry becomes smooth and natural.

Conversion formulas:

degrees → radians = deg × π / 180
radians → degrees = rad × 180 / π

---

### 2️⃣ Rotation (changing direction)
Rotation changes **direction**, not **position**.

Example:  
Point **(1, 0)** rotated **45°** → **(0.707, 0.707)**

---

### 3️⃣ Rotation Matrix
A rotation matrix is a tool that rotates a point in 2D:

[ cosθ −sinθ ]
[ sinθ cosθ ]

Multiplying this matrix by a point rotates the point in space.

---

### 4️⃣ Translation (changing position)
Translation changes **position**, not **direction**.

Example:  
(x, y) translated by (2, 1) → (x + 2, y + 1)

---

### 5️⃣ Rotation + Translation = Transform
When you rotate first and then translate, you get a **2D transform**:

orientation + position = robot pose
rotation + translation = transform

This is how robots represent **where they are**.

---

### 6️⃣ Coordinate Frames (why transforms matter)
Robots never work in a single coordinate system.

Examples:
- `map` → world reference
- `odom` → wheel-based motion estimation
- `base_link` → robot body center
- `camera` → camera location
- `gripper` → end-effector

To convert points between frames:
- apply a transform (rotation + translation)
- Apply the inverse of the transform from the target frame to the source frame.
- Apply the transform from the source frame to the target frame.

This mathematical concept is the foundation of:
- ROS2 `tf2`
- SLAM
- Odometry
- Navigation
- EKF
- Kinematics

---

## 📌 Why This Repo Matters
This project helped me understand:
- How robots represent direction and movement
- How rotation and translation combine into a transform
- How coordinate frames relate to each other in robotics

These fundamentals support every robotics topic I will learn next.

---

## 📚 References

- [Robotics: Modelling, Planning and Control](https://www.amazon.com/Robotics-Modelling-Planning-Control-2nd/dp/0128136963)
- [Robot Operating System (ROS) Tutorials](http://wiki.ros.org/ROS/Tutorials)
