# from timeit import default_timer as timer
# import graphviz
from timer_ import Timer

class Motion_time():

    def __init__(self,
                 name_flow_chart='Flow Process Chart',
                 processes = [
                     'หยิบน็อตตัวผู้',
                     'นำน็อตตัวผู้ใส่บล็อก',
                     'หยิบแหวน',
                     'นำแหวนสวมน็อตตัวผู้',
                     'หยิบน็อตตัวเมีย',
                     'นำน็อตตัวเมียมาประกอบกับน็อตผู้',
                     'โยนเก็บชิ้นงาน'
                 ]):
        # self.num_action_left = num_action_left
        # self.num_action_right = num_action_right
        # self.num_product = num_product

        self.count_action_l = 0 
        self.step_l = 0
        self.all_l = 0

        self.count_action_r = 0 
        self.step_r = 0
        self.all_r = 0

        self.start_l = None
        self.end_l = None
        self.total_l = 0
        self.side_time_l = []
        self.main_time_l = []
        self.all_time_l = []

        self.start_r = None
        self.end_r = None
        self.total_r = 0
        self.side_time_r = []
        self.main_time_r = []
        self.all_time_r = []

        self.time_l_f = Timer()
        self.time_r_f = Timer()

        self.time_study_l = Timer()
        self.time_study_r = Timer()

        self.product_l = 0
        self.product_r = 0

        # for i in range(0,num_action_left):
        #     self.time_study_l[f"Step{i+1}"] = []

        # for i in range(0,num_action_right):
        #     self.time_study_r[f"Step{i+1}"] = []


        # self.dot = graphviz.Digraph(comment = name_flow_chart )

        self.processes = processes

        self.step_proce_r = 0
        self.step_proce_l = 0

        self.id0 = [[161,178], [180,220], [150,169], [138,176]] #dist min -5
        self.id1 = [[145,171], [186,226], [165,179], [120,196]] #sho min -1 elbow max +16 arm min -3
        self.id4 = [[125,145], [185,236], [150,178], [109,140]]
        self.id5 = [[136,180], [200,265], [134,160], [85,113]]
        self.id6 = [[55,106], [70,312], [127,180], [56,325]] #elbow max+31

        self.id10 = [[170,180], [150,185], [150,178], [120,160]]
        self.id11 = [[150,178], [140,183], [165,180], [130,169]] #dist max+5 min-5 sho min -5 arm min -3
        self.id14 = [[132,145], [133,175], [140,179], [109,155]]
        self.id15 = [[135,176], [92,162], [129,165], [70,108]]
        self.id16 = [[34,93], [38,320], [124,179], [65,330]]

        # self.time_poon = []
        # self.stat_poon = Timer()
        # self.end_poon = Timer()
        self.time_poor = Timer()
        self.alert_poon = True

        self.poor_list = {
                'time': [],
                'neck':[],
                'torso':[]
            }

    def duo_move_action_l(self, script_l, sensor_position_l, dis_assemble_l, dis_stone_l):
        num_process_l = len(script_l)
        if self.count_action_l < num_process_l:
            if sensor_position_l == script_l[self.count_action_l]:
                if self.step_l == 0:
                    if self.all_l == 0:
                        self.time_l_f.start()
                        self.all_l = 1
                    self.step_l = 1
                    self.time_study_l.start()
                    self.count_action_l += 1
                    print(f"process_l:{sensor_position_l}")

        if self.step_l == 1:
            if dis_assemble_l <= 32:
                if self.count_action_l < num_process_l:
                    self.step_l = 0
                    self.total_l = round(self.time_study_l.stop(),3)
                    # self.total_l = self.end_l - self.start_l
                    self.side_time_l.append(self.total_l)
                    print(f"wait_l: {self.total_l}")

                else :
                    if self.step_l == 1:
                        self.step_l = 2
                        self.total_l = round(self.time_study_l.stop(),3)
                        self.side_time_l.append(self.total_l)
                        print(f"wait_l: {self.total_l}")
                        self.time_study_l.start()

        if self.count_action_l >= num_process_l:
            if dis_stone_l <= 45:
                if self.step_l == 2:
                    self.step_l = 0
                    if self.all_l == 1:
                        total = round(self.time_l_f.stop(),3)
                        self.all_time_l.append(total)
                        self.all_l = 0
                    self.total_l = round(self.time_study_l.stop(),3)
                    self.count_action_l = 0
                    self.side_time_l.append(self.total_l)
                    print(f"Stone_l: {self.total_l}")
                    self.main_time_l.append(self.side_time_l)
                    self.side_time_l = []

    def duo_move_action_r(self, script_r, sensor_position_r, dis_assemble_r,  dis_stone_r):

        num_process_r = len(script_r)

        if self.count_action_r < num_process_r:
            if sensor_position_r == script_r[self.count_action_r]:
                if self.step_r == 0:
                    if self.all_r == 0:
                        self.time_r_f.start()
                        self.all_r = 1
                    self.step_r = 1
                    self.time_study_r.start()
                    self.count_action_r += 1
                    print(f"process_r:{sensor_position_r}")

        if self.step_r == 1:
            if dis_assemble_r <= 32:
                if self.count_action_r < num_process_r:
                    self.step_r = 0
                    self.total_r = round(self.time_study_r.stop(),3)
                    self.side_time_r.append(self.total_r)
                    print(f"wait_r: {self.total_r}")

                else :
                    if self.step_r == 1:
                        self.step_r = 2
                        self.total_r = round(self.time_study_r.stop(),3)
                        self.side_time_r.append(self.total_r)
                        print(f"wait_r: {self.total_r}")
                        self.time_study_r.start()

        if self.count_action_r >= num_process_r :
            if dis_stone_r <= 45:
                if self.step_r == 2:
                    self.step_r = 0
                    if self.all_r == 1:
                        total = round(self.time_r_f.stop(),3)
                        self.all_time_r.append(total)
                        self.all_r = 0
                    self.total_r = round(self.time_study_r.stop(),3)
                    self.count_action_r = 0
                    self.side_time_r.append(self.total_r)
                    print(f"Stone_r: {self.total_r}")
                    self.main_time_r.append(self.side_time_r)
                    self.side_time_r = []

        
    
    def return_time_l(self):
        return self.main_time_l
    
    def return_time_real_l(self):
        return self.all_time_l
    
    def return_time_r(self):
        return self.main_time_r
    
    def return_time_real_r(self):
        return self.all_time_r
    
    def poor_body(self, alert, neck, torso):
        if alert:
            if self.alert_poon:
                self.alert_poon = False
                self.time_poor.start()
                

        else:
            if not self.alert_poon:
                # self.time_poor.start()
                self.alert_poon = True
                total = round(self.time_poor.stop(),3)
                self.poor_list['time'].append(total)
                self.poor_list['neck'].append(neck)
                self.poor_list['torso'].append(torso)
                
    
    def return_poor_time(self):
        return self.poor_list

    def count_process_r(self):
        return self.step_proce_r
    def count_process_l(self):
        return self.step_proce_l
    
    def count_product(self):
        return [self.product_r,self.product_l]
    
    def body_posture_detection(self,neck_, torso):
        if neck_ >= 48.73 :
            return True
        else:
            return False