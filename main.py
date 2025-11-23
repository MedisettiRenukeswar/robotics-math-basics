from robotics_math import (
    deg2rad,
    rad2deg,
    rotation_matrix_2d,
    apply_rotation_2d,
    transform_point_2d,
    compose_transform_2d,
)


def print_matrix(R, name="R"):
    print(f"{name} = [ [{R[0][0]: .4f}, {R[0][1]: .4f}]")
    print(f"      [ {R[1][0]: .4f}, {R[1][1]: .4f}] ]")


def main():
    print("=== Robotics Math Basics Demo ===\n")

    # 1. Degrees ↔ Radians
    angle_deg = 45.0
    angle_rad = deg2rad(angle_deg)
    print(f"Angle: {angle_deg} deg = {angle_rad:.4f} rad")
    print(f"Back to degrees: {rad2deg(angle_rad):.4f} deg\n")

    # 2. Rotation matrix
    R = rotation_matrix_2d(angle_rad)
    print_matrix(R, "R (45 deg)")

    # 3. Rotate a point
    p = (1.0, 0.0)
    p_rot = apply_rotation_2d(R, p)
    print(f"\nRotate point {p} by 45 deg -> {p_rot}\n")

    # 4. Transform a point with rotation + translation
    t = (2.0, 1.0)
    p_tf = transform_point_2d(R, t, p)
    print(f"Transform point {p} with R (45 deg) and t {t} -> {p_tf}\n")

    # 5. Compose two transforms
    angle2_deg = 30.0
    angle2_rad = deg2rad(angle2_deg)
    R2 = rotation_matrix_2d(angle2_rad)
    t2 = (1.0, -1.0)

    print_matrix(R2, "R2 (30 deg)")

    R_comp, t_comp = compose_transform_2d(R, t, R2, t2)
    print("\nComposed transform R_comp, t_comp:")
    print_matrix(R_comp, "R_comp")
    print(f"t_comp = {t_comp}")

    # 6. Apply composed transform to a point
    p2 = (0.5, 0.5)
    from robotics_math import transform_point_2d as tf

    p2_tf = tf(R_comp, t_comp, p2)
    print(f"\nApply composed transform to point {p2} -> {p2_tf}\n")

    print("=== Demo complete ===")


if __name__ == "__main__":
    main()
